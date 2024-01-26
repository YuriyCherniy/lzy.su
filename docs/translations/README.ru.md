![GitHub top language](https://img.shields.io/github/languages/top/yuriycherniy/lzy.su)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/yuriycherniy/lzy.su)
![GitHub](https://img.shields.io/github/license/yuriycherniy/lzy.su)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/yuriycherniy/lzy.su)
![Static Badge](https://img.shields.io/badge/beginner%20friendly-008080)

_**Выберите язык [ENG](https://github.com/YuriyCherniy/lzy.su)/RUS**_
# Привет! #
Вы находитесь за кулисами сервиса сокращения ссылок [lzy.su](https://lzy.su/). Это небольшой, но полнофункциональный сервис. С помощью сервиса вы можете сокращать URL-адреса и управлять короткими ссылками без регистрации и даже получать статистику переходов по коротким ссылкам. Сервис создан с использованием веб-фреймворка Django. Простота сервиса позволяет легко понять исходный код пользователям практически с любым опытом программирования. За работу сервиса отвечают всего несколько представлений, пара моделей и один простой валидатор.

И еще одна мелочь. Этот проект был создан, чтобы предложить новый способ создания и управления короткими URL-адресами не похожий на другие сервисы. Как создать ленивый короткий URL читайте здесь: [lzy.su](https://lzy.su/). Просто попробуйте, вам понравится.

### Чтобы запустить локально, выполните обычные действие: ###

Создайте виртуальное окружение Python 3.10.x, 3.11.x или 3.12.x:
```
python3 -m venv .venv
```
Активируйте виртуальное окружение:
```
source .venv/bin/activate
```
Клонируйте репозиторий:
```
git clone https://github.com/YuriyCherniy/lzy.su.git
```
Перейдите в рабочую директорию:
```
cd lzy.su/
```
Установите зависимости:
```
pip install -r requirements/dev.txt
```
Скопируйте содержимое ```.env.example``` в ```.env```:
```
cp .env.example .env
```
Выполните миграции:
```
./manage.py migrate
```
Создайте супер пользователя:
```
./manage.py createsuperuser
```
Запустите сервер:
```
./manage.py runserver
```