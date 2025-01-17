# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (optional for APIs)
EXPOSE 8000

# Default command (can be overridden by docker-compose.yml)
CMD ["python", "psql/main.py"]
