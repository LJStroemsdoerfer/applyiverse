FROM ubuntu:latest

# create directory
RUN mkdir -p /showcase

# update packages
RUN apt-get update -y

# install apt-utils
RUN apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y software-properties-common \
    && apt-get install -y gnupg2 \
    && apt-get install -y tzdata \
    && apt-get install -y libssl-dev \
    && apt-get install -y libcurl4-gnutls-dev

# set the time zone
ENV TZ Europe/Berlin

# install pip
RUN apt-get install -y python3-pip

# copy files
COPY cryptocast/ showcase/cryptocast
COPY api.py /showcase/api.py
COPY requirements.txt /showcase/requirements.txt

# install all packages
RUN python3 -m pip install -r /showcase/requirements.txt

# expose ports
EXPOSE 5555

# run API
ENTRYPOINT ["python3", "showcase/api.py"]