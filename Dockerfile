FROM ubuntu:18.04

RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt && \
    pip3 install lxml

RUN python3 -m nltk.downloader punkt && \
    python3 -m nltk.downloader stopwords

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]