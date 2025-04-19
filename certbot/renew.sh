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

log "Running certbot renew..."
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet
if [ $? -ne 0 ]; then
    log_err "Certificate renewal failed!"
    exit 2
else
    log "Certificate renewal completed successfully."
fi

log "Switching to lzy.su directory..."
cd "${HOME}/lzy.su"
if [ $? -ne 0 ]; then
    log_err "Failed to switch to lzy.su directory!"
    exit 3
fi

log "Reloading nginx..."
docker compose exec nginx nginx -s reload
if [ $? -ne 0 ]; then
    log_err "nginx reload failed!"
    exit 4
else
    log "nginx reload completed successfully."
fi

log "=== Certificate renewal process finished ==="