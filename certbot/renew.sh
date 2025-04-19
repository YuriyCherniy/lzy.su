#!/bin/bash

log() {
    echo "[ $(date '+%Y-%m-%d %H:%M:%S') ] $1"
}
log_err() {
    echo "[ $(date '+%Y-%m-%d %H:%M:%S') ] ERROR: $1" >&2
}

log "=== Certificate renewal process started ==="

log "Switching to certbot directory..."
cd "${HOME}/lzy.su/certbot"
if [ $? -ne 0 ]; then
    log_err "Failed to switch to certbot directory!"
    exit 1
fi

log "Running certbot renew (nginx will reload only if certificate is renewed)..."
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet \
    --deploy-hook "echo '[ $(date '+%Y-%m-%d %H:%M:%S') ] Deploy hook: reloading nginx...' && cd /home/dock/lzy.su && docker compose exec nginx nginx -s reload && echo '[ $(date '+%Y-%m-%d %H:%M:%S') ] Deploy hook: nginx reload completed.'"
if [ $? -ne 0 ]; then
    log_err "Certificate renewal failed!"
    exit 2
else
    log "Certificate renewal process finished. If certificate was renewed, nginx was reloaded."
fi

log "=== Certificate renewal process finished ==="