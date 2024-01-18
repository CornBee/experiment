# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the sender script into the container at /app
COPY sender.py /app

# When the container launches, run the sender.py script
CMD ["python", "./sender.py"]
