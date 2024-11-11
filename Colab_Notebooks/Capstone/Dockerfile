# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install ObsPy
RUN pip install obspy

# Copy the current directory contents into the container at /app
COPY . /app

# Run the process_seismic_data.py script by default when the container starts
CMD ["python", "process_seismic_data.py"]

