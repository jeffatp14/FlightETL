FROM python:3.12
WORKDIR /opt/FlightETL

LABEL authors="dzno9"

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into container
COPY . .

ENTRYPOINT [ "python", "/opt/FlightETL/main.py" ]