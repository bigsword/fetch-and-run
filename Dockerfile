FROM python:latest
RUN pip install boto3 psycopg2
WORKDIR /usr/local/bin
COPY fetch_and_run.py .
USER nobody
CMD ["python", "fetch_and_run.py"]