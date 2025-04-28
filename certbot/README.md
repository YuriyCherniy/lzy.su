To obtain certificates before running docker compose to start the whole project run command:

```docker compose run --rm --service-ports certbot certonly --standalone -d mydomain.ru -d www.mydomain.ru```

To renew existing certificates manually when project is already running. Nginx must be running and reloaded after renewal.
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt

create cron job to renew certificates automatically:
python3 /path/to/script/renew.py >> /var/log/certbot-renew.log 2>&1