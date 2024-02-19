# Bryntum Grid with Django REST framework

This repository contains code to help you build a Bryntum Grid integrated with Django REST framework.

## Getting started

In the root folder create a virtual environment using the following command:

```sh
python -m venv venv
```

Activate the virtual environment in your shell with the following command:

```sh
source venv/bin/activate
```

Install Django and Django REST framework:

```sh
pip install django djangorestframework
```

Copy the following files and folders from the `/build` folder in the Bryntum Grid distribution folder and paste them in the `playerinfo/static/bryntum-grid` folder:

- `fonts`
- `locales` 
- `grid.module.js` 
- `grid.module.js.map`
- `grid.stockholm.css` 
- `grid.stockholm.css.map` 

Preview the app at [http://localhost:8000](http://localhost:8000) by running the following command:

```sh
python manage.py runserver localhost:8000
```