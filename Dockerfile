FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py migrate && \
    python manage.py collectstatic --noinput
CMD python manage.py createsuperuser --noinput --username admin --email '' 2>/dev/null || true && \
    gunicorn --bind 0.0.0.0:8000 --workers 3 core.wsgi:application