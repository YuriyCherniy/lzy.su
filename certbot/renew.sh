#!/bin/bash
cd /dock/lzy.su/certbot
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet && \
cd /dock/lzy.su && \
docker compose exec nginx nginx -s reload