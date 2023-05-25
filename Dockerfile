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

# Expose port
EXPOSE 5000

CMD ["python3", "application.py"]

# New Relic Agent
RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="BlackList_PRD"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true

# INGEST_License
ENV NEW_RELIC_LICENSE_KEY=a84e6be62d46acc823750b60bea76f5e5c1cNRAL
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT ["newrelic-admin", "run-program"]