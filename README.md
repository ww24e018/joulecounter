# joulecounter

might build with:

```
export DJANGO_SUPERUSER_PASSWORD=MySecret

docker-compose up --build
```

llm says
```
SECRET_KEY=$(openssl rand -hex 40) docker-compose up --build
```
if one wants a fixed secret for a container build.

env DJANGO_ALLOWED_HOSTS another config

```
export CSRF_TRUSTED_ORIGINS=https://myurl.com
```
