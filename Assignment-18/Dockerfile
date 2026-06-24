FROM python:3.12-slim

# Install Java
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk && \
    apt-get clean

# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install PySpark
RUN pip install pyspark

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]