FROM python:3.8-slim

WORKDIR /app

# Copy and install the requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code into the container
COPY . .

EXPOSE 5000

# Define environment variable
ENV NAME SentimentAnalysis

# Run app.py when the container launches
CMD ["python", "app.py"]
