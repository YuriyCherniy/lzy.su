# lzy.su #

This project has been created to offer a new way to create and manage short URLs. How to create lazy short URL read here: [lzy.su](https://lzy.su/). If you try it out, you will like it.

### To run locally, do the usual: ###

Create a Python virtual environment:
```
python3 -m venv .venv
```
Activate virtual environment:
```
source .venv/bin/activate
```
Clone repository:
```
git clone https://github.com/YuriyCherniy/lzy.su.git
```
cd to working directory:
```
cd lzy.su/
```
Install dependencies:
```
pip install -r requirements/dev.txt
```
Rename ```.env.example``` to ```.env```:
```
mv .env.example .env
```

Create Postgres database:
```
sudo -u postgres psql
```
```
CREATE DATABASE lazy_url_db;
```
```
CREATE USER lazy_url_user WITH PASSWORD '0000';
```
```
GRANT ALL PRIVILEGES ON DATABASE lazy_url_db TO lazy_url_user;
```
Exit Postgres console ```ctr+Z```
Make migrations:
```
./manage.py makemigrations
```
Migrate:
```
./manage.py migrate
```
