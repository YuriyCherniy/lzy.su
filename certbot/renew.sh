#!/bin/bash
cd $HOME/lzy.su/certbot
docker compose run --rm certbot renew --quiet && \
docker compose exec lzysu-nginx-1 nginx -s reload