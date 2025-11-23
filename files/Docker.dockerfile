# 1. Use an official, lightweight Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy and install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code into the container
COPY . .

# 5. Expose the port that uvicorn will run on
EXPOSE 8000

# 6. The command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]