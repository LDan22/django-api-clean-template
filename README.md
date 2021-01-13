# Django REST clean template
### Django template for RESTful Web Services

*This is a clean template for fast deployment and development of a project*

Used tools and libraries:
- Django REST Framework
- Django REST Knox (Token authentication)
- DRF-YASG (swagger)
- Docker

Template contains docker and nginx settings for both development and production.

### *Be sure you have installed docker on your system*

> Guideline:
1. development: `docker-compose up -d --build` 
2. production:  `docker-compose -f docker-compose.prod.yml up --build`

When you start project, automatically are run and other commands, such as:
`python manage.py migrate`, `python manage.py flush`, `python manage.py collectstatic`

You can control which commands to run initially, in entrypoint.sh or entrypoint.prod.sh, depending on mode you are on.

> Some people can have an error if `.sh` files do not have UNIX endings. You can
>convert them to right format using Notepad++