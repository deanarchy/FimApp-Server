# FimApp-Server
This is FimApp server, a Financial Manager apps. This repo intended as a backend part of the FimApp project. It contains a several apps and APIs endpoints to exhibit a certain functionality. It was built mainly by using Django REST Framework.

## Full Demo
[FimApp](https://fimapp.vercel.app/)

## Local Installation 
**1. Make sure you already have Docker and Docker Compose properly installed**

[Get Docker](https://docs.docker.com/get-docker/)

**2. Clone repos**

```bash
  git clone https://github.com/deanarchy/FimApp-Server.git
```

**3. Run Docker Compose with Development config**
```bash
  docker-compose up -f docker-compose.yml -d --build
```

**4. Migrate the database**
```bash
  docker-compose exec backend python manage.py migrate
```

**5. Create superuser**
```bash
  docker-compose exec backend python manage.py createsuperuser
```

## Documentation
To be added...

## Credits
This server mainly built using [Django REST Framework](https://www.django-rest-framework.org/)

[dj-rest-auth](https://github.com/iMerica/dj-rest-auth) used for authentication systems.

[django-rest-framework-simplejwt](https://github.com/jazzband/django-rest-framework-simplejwt) used for JSON Web Token authentication.
