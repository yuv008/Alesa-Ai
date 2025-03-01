# Use an official lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first for efficient caching
COPY requirements.txt .

# Install dependencies without using cache
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose a port (if running a web app)
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py"]
