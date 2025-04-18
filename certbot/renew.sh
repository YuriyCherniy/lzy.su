#!/bin/bash
echo test
cd /home/dock/lzy.su/certbot
echo test
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet && \
cd /home/dock/lzy.su && \
docker compose exec nginx nginx -s reload
echo test