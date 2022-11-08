# New Project Library

## Run project 
```bash 
python manage.py runserver 
#$ Alternative 
python manage.py runserver 5000
```
# Default Database
```bash 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
## Mongodb with django and postgres "docker"
```bash 
# Use mongo on docker
docker run --name mongodb -e MONGODB_USER=kartien -e MONGODB_PASSWORD=mischuros2 -p 27017:27017 -d mongo
# Use postgres on docker 
docker run --name some-postgres -e POSTGRES_USER=your-user -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -d postgres

```
## Connect postgress
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'kartien',
        'PASSWORD': 'mischuros2',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## MVT
