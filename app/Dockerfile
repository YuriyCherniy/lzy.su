FROM python:3.11
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY requirements/base.txt requirements/prod.txt requirements/
RUN pip3 install -r requirements/prod.txt
COPY . .
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT [ "./docker-entrypoint.sh" ]
