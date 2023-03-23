FROM alpine:latest
WORKDIR /opt/politzekbot
COPY . /opt/politzekbot
RUN apk --no-cache add python3 py3-pip
RUN pip3 install -r /opt/politzekbot/requirements.txt
ENTRYPOINT [ "/usr/bin/python3", "/opt/politzekbot/main.py" ]
