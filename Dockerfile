FROM python:3.8-slim

WORKDIR /app

<<<<<<< HEAD
# Copy only the necessary files first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Remove unnecessary files to reduce image size
RUN rm -rf __pycache__ .DS_Store venv .git

=======
# Copy and install the requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code into the container
COPY . .

>>>>>>> 1dba52abeb86358e14ad09c41672dfc8341ea0ac
EXPOSE 5000

# Define environment variable
ENV NAME SentimentAnalysis

# Run app.py when the container launches
CMD ["python", "app.py"]
