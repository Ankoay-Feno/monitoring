FROM alpine:latest

RUN apk add --no-cache wget unzip

# Télécharger Loki
RUN wget https://github.com/grafana/loki/releases/download/v2.9.0/loki-linux-amd64.zip
RUN unzip loki-linux-amd64.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/loki-linux-amd64

# Télécharger Alertmanager
RUN wget https://github.com/prometheus/alertmanager/releases/download/v0.25.0/alertmanager-0.25.0.linux-amd64.tar.gz
RUN tar xvfz alertmanager-*.tar.gz
RUN cp alertmanager-0.25.0.linux-amd64/alertmanager /usr/local/bin/

COPY loki-config.yml /etc/loki/config.yml
COPY alertmanager.yml /etc/alertmanager/config.yml

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]