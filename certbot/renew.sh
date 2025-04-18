#!/bin/bash
cd /home/dock/lzy.su/certbot
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet && \
cd /home/dock/lzy.su && \
docker compose exec nginx nginx -s reload