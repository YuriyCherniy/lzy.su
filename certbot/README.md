To obtain certificates, before running docker compose to start the whole project, run the command:

```
docker compose run --rm --service-ports certbot certonly --standalone -d mydomain.ru -d www.mydomain.ru
```

To renew existing certificates manually, when the project is already running (Nginx must be running, and reloaded after renewal), run the command:

```
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt
```

To create a cron job to renew certificates automatically, add the following line to the crontab:

```
0 0 * * * python3 ~/lzy.su/certbot/renew.py >> /var/log/certbot-renew.log 2>&1
```
