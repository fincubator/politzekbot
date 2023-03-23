FROM alpine:latest
WORKDIR /opt/politzekbot
RUN apk --no-cache add python3 py3-pip
COPY . /opt/politzekbot
RUN pip3 install -r /opt/politzekbot/requirements.txt
ENTRYPOINT [ "/opt/politzekbot/wrapper.sh" ]
