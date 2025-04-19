#!/bin/bash
LOGFILE="${HOME}/lzy.su/certbot/renew.log"
echo "[ $(date) ] === Начало обновления сертификата ===" | tee -a "$LOGFILE"

# Переход в директорию certbot
cd ${HOME}/lzy.su/certbot
if [ $? -eq 0 ]; then
    echo "[ $(date) ] Перешёл в директорию certbot." | tee -a "$LOGFILE"
else
    echo "[ $(date) ] Ошибка перехода в директорию certbot!" | tee -a "$LOGFILE"
    exit 1
fi

# Запуск обновления сертификата
echo "[ $(date) ] Запуск certbot renew..." | tee -a "$LOGFILE"
docker compose run --rm certbot renew --webroot -w /etc/letsencrypt --quiet 2>&1 | tee -a "$LOGFILE"
if [ $? -eq 0 ]; then
    echo "[ $(date) ] Certbot renew завершён успешно." | tee -a "$LOGFILE"
else
    echo "[ $(date) ] Ошибка при обновлении сертификата!" | tee -a "$LOGFILE"
    exit 2
fi

# Переход в директорию lzy.su
cd ${HOME}/lzy.su
if [ $? -eq 0 ]; then
    echo "[ $(date) ] Перешёл в директорию lzy.su." | tee -a "$LOGFILE"
else
    echo "[ $(date) ] Ошибка перехода в директорию lzy.su!" | tee -a "$LOGFILE"
    exit 3
fi

# Перезапуск nginx
echo "[ $(date) ] Перезапуск nginx..." | tee -a "$LOGFILE"
docker compose exec nginx nginx -s reload 2>&1 | tee -a "$LOGFILE"
if [ $? -eq 0 ]; then
    echo "[ $(date) ] Перезапуск nginx завершён." | tee -a "$LOGFILE"
else
    echo "[ $(date) ] Ошибка перезапуска nginx!" | tee -a "$LOGFILE"
    exit 4
fi

echo "[ $(date) ] === Конец обновления сертификата ===\n" | tee -a "$LOGFILE"