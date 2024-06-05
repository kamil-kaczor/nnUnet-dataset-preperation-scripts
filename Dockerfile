# Dockerfile forked from: https://github.com/josegcpa/nnunet_docker
# Modifications:
# - Removed USER root
# - Added update of packages
# - Added installation of git bash and unzip

FROM python:3.11.4-slim-bullseye
WORKDIR /nnunet_pred_folder

# install environment
RUN pip install pip setuptools wheel
COPY requirements.txt ./
RUN pip install -r requirements.txt

# update and install packages
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install git bash && \
    apt-get -y install unzip

# create accessory directories
RUN mkdir /model && \
    mkdir -p /data && \
    mkdir -p /data/input && \
    mkdir -p /data/output && \
    mkdir -p utils