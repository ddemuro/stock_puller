FROM --platform=linux/amd64 python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app
ENV INFILE=m1data.csv
ENV OUTFILE=m1data_out.csv

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "process_csv_data.py", "-i", "m1data.csv", "-o", "m1data_out.csv"]