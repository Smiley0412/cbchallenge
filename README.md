# Messaging App

## Backend

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver localhost:8000
```

Backend server is hosted on http://localhost:8000

## Frontend

```bash
cd frontend
cp .env.local.sample .env.local
yarn install
yarn serve
```

Frontend server is hosted on http://localhost:8080

## Testing

>Please visit to http://localhost:8080 and Enjoy!

## Technologies for this app.

>Django Rest Framework, Auth Token, Channels, Websockets, Vue 3, Axios, Moment, UIkit, Vue Toast Notification, 