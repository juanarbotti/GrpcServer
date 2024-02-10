FROM debian:12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Etiquetas
LABEL description="Grpc Server Example"

# Defines Localization settings (for Argentina)
ENV LC_ALL es_AR.UTF-8
ENV LANG es_AR.UTF-8
ENV LANGUAGE es_AR.UTF-8

# Install packages
RUN \
    apt-get update && \
    apt-get install gcc locales locales-all build-essential python3-dev python3-venv -y

# Creates a symbolic link to timezone configuration
RUN ln -sf /usr/share/zoneinfo/America/Buenos_Aires /etc/localtime

# Creates app directory
RUN mkdir -p /app

# Stablish working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app

# Activates venv and install requirements
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"

# Copia the rest of the application
COPY src .

# Runs the application
CMD /app/venv/bin/python3 /app/run.py