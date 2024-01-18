# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the receiver script into the container at /app
COPY receiver.py /app

# When the container launches, run the receiver.py script
CMD ["python", "./receiver.py"]
