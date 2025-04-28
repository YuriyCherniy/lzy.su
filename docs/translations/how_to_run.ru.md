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