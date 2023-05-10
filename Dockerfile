# Pull official base image
FROM python:3.9-slim-buster

# Set work directory
WORKDIR /app

# Set enviroment variables
ENV DATABASE_URL postgresql://postgres:ABCD1234@db-black-list.cqhvrt5vquda.us-east-1.rds.amazonaws.com:5432/postgres

# Install pip requirements
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt

# Copy Project
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 5000

CMD ["python3", "application.py"]