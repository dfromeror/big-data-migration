# big-data-migration

A simple project for tech challenge.

## Preconditions:

- Python 3.9.6

## Clone the project

```
git clone https://github.com/dfromeror/big-data-migration
```

## Run local

### Move app folder

```
cd app
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:9000/docs
```