#!/bin/bash
cd $HOME/lzy.su/certbot
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet && \
docker compose exec nginx nginx -s reload