# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY add-date.py .

# Install necessary packages
RUN pip install Pillow moviepy

# Run the Python script with a command-line argument when the container launches
CMD ["python", "add-date.py", "/app/src"]
