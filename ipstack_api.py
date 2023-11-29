from requests.exceptions import RequestException
import requests
import logging
import sys

class IPStackAPI:
    BASE_URL = "http://api.ipstack.com/"

    def __init__(self, access_key):
        if not hasattr(self, '_access_key'):
            self._access_key = access_key
        else:
            raise ValueError("Access key is already set and is immutable.")

    @property
    def access_key(self):
        return self._access_key

    @staticmethod
    def make_request(url, verb='GET', data=None, retries=3):
        """
        Static method to make HTTP request.
        """
        method = getattr(requests, verb.lower(), None)
        if not method:
            raise ValueError("Invalid HTTP verb")

        last_error = None
        for _ in range(retries):
            try:
                response = method(url, json=data)
                logging.debug(f"HTTP {verb} Request to {url} - Status Code: {response.status_code}")

                if 500 <= response.status_code < 600:
                    logging.warning(f"Server error encountered. Retrying...")
                else:
                    response.raise_for_status()
                    return response.json()

            except RequestException as e:
                last_error = str(e)
                logging.error(f"HTTP request error: {last_error}")

        logging.error("Max retries reached or client error occurred.")
        sys.exit()

    def ipstack_ip_location_lookup(self, ip_address):
        url = f"{self.BASE_URL}{ip_address}?access_key={self._access_key}&output=json"
        return self.make_request(url, verb='GET')

    def ipstack_bulk_ip_location_lookup(self, ip_addresses):
        ip_list = ','.join(ip_addresses)
        url = f"{self.BASE_URL}{ip_list}?access_key={self._access_key}&output=json"
        return self.make_request(url, verb='GET')
