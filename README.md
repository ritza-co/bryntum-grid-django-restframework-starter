# Bryntum Grid with Django REST framework

This repository contains code to help you build a Bryntum Grid integrated with Django REST framework. The code for the completed app is in the `complete-app` branch. To run this app, clone the repo and switch to the `complete-app` branch before following the steps below.

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

Make and run the migrations:

```sh
python manage.py makemigrations 
python manage.py migrate
```

Then add some data to the SQLite database:

```sh
sqlite3 db.sqlite3
```

```sql
INSERT INTO api_player (name, city, team, score, percentage_wins) VALUES 
('Dan Jones', 'Los Angeles', 'Stockholm Eagles', 430, 30),
('Harry Smith', 'Dubai', 'Paris Lions', 120, 50),
('Peter Holmes', 'Stockholm', 'Washington Ducks', 90, 55),
('Jacob Reese', 'Moscow', 'Washington Ducks', 500, 43),
('Gilles Girard', 'Paris', 'Moscow Bears', 800, 88),
('Dan Jacobsen', 'Moscow', 'Paris Lions', 920, 93),
('Walter Cruise', 'Barcelona', 'Stockholm Eagles', 100, 44),
('Bill Nielsen', 'Madrid', 'Stockholm Eagles', 750, 55),
('Gareth Freeman', 'Chicago', 'Moscow Bears', 310, 33),
('Ben Newman', 'Los Angeles', 'Washington Ducks', 670, 66),
('Garry Miller', 'Paris', 'Paris Lions', 820, 80),
('Jim Knowles', 'Dubai', 'Stockholm Eagles', 440, 53),
('Victor Reddy', 'London', 'Moscow Bears', 960, 93),
('Bradley May', 'Los Angeles', 'Stockholm Eagles', 200, 40),
('Wesley Malone', 'Berlin', 'Washington Ducks', 760, 29);
```

Download the Bryntum Grid distribution folder [here](https://customerzone.bryntum.com/).

If you don't have a license for the Bryntum Grid, download the trial version [here](https://bryntum.com/download/). From the `/build` folder, copy the following files to the `static/bryntum-grid` folder:

```
fonts
locales
grid.module.js
grid.module.js.map
grid.stockholm.css
grid.stockholm.css.map
```

Run the development server with:

```sh
python manage.py runserver localhost:8000
```

This will start a local server at `http://localhost:8000` and you can view the Grid app.