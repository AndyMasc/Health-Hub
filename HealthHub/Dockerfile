FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py collectstatic --noinput

CMD ["gunicorn", "HealthHub.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "--threads", "2"]
