# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    unixodbc-dev \
    gcc \
    g++ \
    libffi-dev \
    curl

# Install ODBC Driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "run.py"]
