_**Choose language ENG/[RUS](https://github.com/YuriyCherniy/lzy.su/blob/main/docs/translations/how_to_run.ru.md)**_

### To run locally, do the usual: ###

Create a Python 3.10.x, 3.11.x or 3.12.x virtual environment:
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