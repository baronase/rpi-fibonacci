# Use a base image that works on ARM architecture
FROM arm32v7/python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask server
CMD ["python", "app.py"]

