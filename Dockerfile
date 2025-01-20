# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Set PYTHONPATH to include the working directory
ENV PYTHONPATH=/app

# Install system dependencies for psycopg2 and PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "psql_dev/main.py"]
