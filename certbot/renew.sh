#!/bin/bash
LOGFILE="${HOME}/lzy.su/certbot/renew.log"
echo "[ $(date) ] === Начало обновления сертификата ===" | tee -a "$LOGFILE"
cd ${HOME}/lzy.su/certbot
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet && \
cd ${HOME}/lzy.su && \
docker compose exec nginx nginx -s reload