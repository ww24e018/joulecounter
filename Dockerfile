FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ARG CSRF_TRUSTED_ORIGINS
ENV CSRF_TRUSTED_ORIGINS=${CSRF_TRUSTED_ORIGINS}
ARG DJANGO_ADMIN_PASS
ENV DJANGO_ADMIN_PASS=${DJANGO_ADMIN_PASS}
RUN python manage.py migrate && \
    python manage.py collectstatic --noinput
CMD python manage.py createsuperuser --noinput --username admin --email '' 2>/dev/null || true && \
    gunicorn --bind 0.0.0.0:8010 --workers 3 joulecounter.wsgi:application