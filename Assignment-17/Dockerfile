FROM python:3.12-slim

# Install Java
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk && \
    apt-get clean

# Java Environment
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /app

# Copy files
COPY . /app

# Install PySpark
RUN pip install --no-cache-dir -r requirements.txt

# Run application automatically
CMD ["python", "app.py"]