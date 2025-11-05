#FROM ubuntu:latest
# Dockerfile, Image, Container
FROM python:3.12
WORKDIR /opt/FlightETL

LABEL authors="dzno9"

# Copy requirements first (better for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into container
COPY . .

ENTRYPOINT [ "python", "/opt/FlightETL/main.py" ]
#ENTRYPOINT ["top", "-b"]