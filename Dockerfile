# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python script into the container
COPY add-date.py .

# Install necessary packages with specific versions
RUN pip install Pillow==9.5.0 moviepy==1.0.3 && \
    pip list && \
    python -c "import moviepy; print(moviepy.__file__)"

# Run the Python script with a command-line argument when the container launches
CMD ["python", "add-date.py", "/app/src"]
