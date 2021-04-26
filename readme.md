# Tell API

Tell API written with FastAPI Python and needs Python 3.6+ <br>
This API requires MongoDB as the Database.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
1. Create virtual environment

2. Execute these command
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload --port 5000
```

## Beat and Worker
- Worker
```bash
celery -A app.cores.celery_init.app worker --loglevel=info
```

- Beat (Automated Tasks)
```bash
celery -A app.cores.celery_init.app beat --schedule /tmp/celerybeatschedule --loglevel=info --pidfile /tmp/celerybeat.pid
```