_**Choose language ENG/[RUS](https://github.com/YuriyCherniy/lzy.su/blob/dev_lzy_v1_2_1/translations/README.md)**_
# Hi there! #
You are behind the scenes of the [lzy.su](https://lzy.su/) link shortening service. This is a small but full-featured service. You can shorten URL and manage short links without registration and even get some click statistics. It's built with Django web framework. The simplicity of the service makes it easy to understand the source code. There are only several Views, a couple Models and one simple Validator.

And there's one more thing. This project has been created to offer a new way to create and manage short URLs. How to create lazy short URL read here: [lzy.su](https://lzy.su/). If you try it out, you will like it.

### To run locally, do the usual: ###

Create a Python 3.8 virtual environment:
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
Copy ```.env.example``` to ```.env```:
```
cp .env.example .env
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
Create a superuser:
```
./manage.py createsuperuser
```
Run server:
```
./manage.py runserver
```