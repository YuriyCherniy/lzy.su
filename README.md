![GitHub](https://img.shields.io/github/license/yuriycherniy/lzy.su)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/yuriycherniy/lzy.su)
![Static Badge](https://img.shields.io/badge/beginner%20friendly-8A2BE2)

_**Choose language ENG/[RUS](https://github.com/YuriyCherniy/lzy.su/blob/main/docs/translations/README.ru.md)**_
# Hi there! #
You're behind the scenes of the [lzy.su](https://lzy.su/) link shortening service. This is a small but full-featured service. You can shorten URLs and manage short links without registration and even get some click statistics. It's built with Django web framework. The simplicity of the service makes it easy to understand the source code by users with almost any programming experience. There are only several Views, a couple Models and one simple Validator.

And there's one more thing. This project has been created to offer a new way to create and manage short URLs. How to create lazy short URL read here: [lzy.su](https://lzy.su/). If you try it out, you will like it.

### To run locally, do the usual: ###

Create a Python 3.8+ virtual environment:
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