FROM python:3.10.5-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY requirements/base.txt requirements/base.txt
# COPY requirements/prod.txt requirements.txt
COPY requirements/prod.txt requirements/prod.txt
# RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements/prod.txt
COPY . .
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT [ "./docker-entrypoint.sh" ]