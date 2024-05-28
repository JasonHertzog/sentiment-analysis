FROM python:3.8-slim

WORKDIR /app

# Copy only the necessary files first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Remove unnecessary files to reduce image size
RUN rm -rf __pycache__ .DS_Store venv .git

EXPOSE 5000

# Define environment variable
ENV NAME SentimentAnalysis

# Run app.py when the container launches
CMD ["python", "app.py"]
