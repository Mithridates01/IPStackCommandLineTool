

# IPStack CLI Tool

A simple and efficient command-line utility for retrieving geolocation data for IP addresses using the [IPStack API](https://ipstack.com/).

## Summary

This tool allows users to quickly obtain geolocation information for one or multiple IP addresses from the command line. It interfaces with the IPStack API to fetch details like continent, country, region, city, zip code, latitude, longitude, and other location-specific information.

PLEASE NOTE: Querying location details for multiple IPs at a single time requires the paid version of the API Key.

## Installation and Setup

### Prerequisites
- Docker installed on your system
- IPStack API access key

### Steps
1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/ipstack-cli-tool.git
    cd ipstack-cli-tool
    ```

2. **Set the IPStack Access Key**
    - Open the `docker-compose.yaml` file.
    - Locate the line `- IPSTACKACCESSKEY=access_key` and replace `access_key` with your actual IPStack API access key.

3. **Build and Run with Docker Compose**
    - Run the following command to build and start the tool:
        ```bash
        docker-compose up
        ```

## Usage Examples

- **Fetching GPS Coordinates for a Single IP Address**
    ```bash
    docker-compose run ipstack-cli-tool --locate_ips 23.223.11.22
    ```
    ```
    (12.971599578857422,77.59459686279297)
    ```
- **Fetching GPS Coordinates for a Multiple IP Addresses**
    
    ***Command***
    ```bash
    docker-compose run ipstack-cli-tool --locate_ips 23.223.11.22,12.29.42.5,8.8.8.8
    ```
    ***Output***
    ```
    {"23.223.11.22":"(12.971599578857422,77.59459686279297)","12.29.42.5":"(12.971599578857422,77.59459686279297)","8.8.8.8":"(12.971599578857422,77.59459686279297)"}
    ```


- **Fetching Full Location Data in JSON Format for a Single IP Address**
    
    ***Command***
    ```bash
    docker-compose run ipstack-cli-tool --locate_ips 23.223.11.22 --full
    ```
    ***Output***
    ```
    {"23.223.11.22": {"ip": "23.223.11.22", "type": "ipv4", "continent_code": "AS", "continent_name": "Asia", "country_code": "IN", "country_name": "India", "region_code": "KA", "region_name": "Karnataka", "city": "Bengaluru", "zip": "560001", "latitude": 12.971599578857422, "longitude": 77.59459686279297, "location": {"geoname_id": 1277333, "capital": "New Delhi", "languages": [{"code": "hi", "name": "Hindi", "native": "\u0939\u093f\u0928\u094d\u0926\u0940"}, {"code": "en", "name": "English", "native": "English"}], "country_flag": "https://assets.ipstack.com/flags/in.svg", "country_flag_emoji": "\ud83c\uddee\ud83c\uddf3", "country_flag_emoji_unicode": "U+1F1EE U+1F1F3", "calling_code": "91", "is_eu": false}}}
    ```
- **Fetching Full Location Data in JSON Format for a Multiple IP Address**

***Command***

    ```bash
    docker-compose run ipstack-cli-tool --locate_ips 23.223.11.22,12.29.42.5,8.8.8.8 --full
    ```
    
***Output***

    ```
    {"23.223.11.22": {"ip": "23.223.11.22", "type": "ipv4", "continent_code": "AS", "continent_name": "Asia", "country_code": "IN", "country_name": "India", "region_code": "KA", "region_name": "Karnataka", "city": "Bengaluru", "zip": "560001", "latitude": 12.971599578857422, "longitude": 77.59459686279297, "location": {"geoname_id": 1277333, "capital": "New Delhi", "languages": [{"code": "hi", "name": "Hindi", "native": "\u0939\u093f\u0928\u094d\u0926\u0940"}, {"code": "en", "name": "English", "native": "English"}], "country_flag": "https://assets.ipstack.com/flags/in.svg", "country_flag_emoji": "\ud83c\uddee\ud83c\uddf3", "country_flag_emoji_unicode": "U+1F1EE U+1F1F3", "calling_code": "91", "is_eu": false}},...additionalIpDetails...}
    ```


## License

This project is licensed under [MIT License](LICENSE).
