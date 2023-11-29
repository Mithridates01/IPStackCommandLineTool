# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/ipstackiptool

# Copy the current directory contents into the container at /usr/src/ipstackiptool
COPY . /usr/src/ipstackiptool

# Install any additional needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the Python script when the container launches
ENTRYPOINT ["python3", "./main.py"]
CMD ["--help"]
