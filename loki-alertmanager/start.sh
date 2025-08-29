#!/bin/bash
# start.sh
/usr/local/bin/loki-linux-amd64 -config.file=/etc/loki/config.yml &
/usr/local/bin/alertmanager --config.file=/etc/alertmanager/config.yml &
wait