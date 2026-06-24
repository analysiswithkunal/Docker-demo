FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y openjdk-21-jdk && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

RUN pip install pyspark

WORKDIR /app

COPY /app.py .
COPY /data/employee.csv .

CMD ["python", "app.py"]