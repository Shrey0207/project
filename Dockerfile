 # Use an official lightweight Python image
FROM python:3.11-slim

# Set a working directory inside the container
WORKDIR /app

# Copy your code and requirements into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "jwt_api_server.py"]
