# iMi-market

## Project Setup

* [Python 3.10.8](https://www.python.org/downloads/release/python-3108/).
* [pip](https://pip.pypa.io/en/stable/installing/).
* [Virtuelenv](https://pypi.org/project/virtualenv/).
* [Postgresql](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

### Clone repo

```shell
git clone https://github.com/iMi-groups/imi-market-api.git
cd imi-market-api
```

### Setting up virtuelenv

```shell
virtualenv venv
```

#### Windows

```shell
venv\Scripts\activate
```

#### Linux

```shell
source venv/bin/activate
```

### Install dependencies

```shell
pip install -r requirements.txt
```

### Collect static files

```shell
python manage.py collectstatic | python3 manage.py collectstatic
```

### Apply Migrations

```shell
python manage.py makemigrations
```

### Apply All database changes

```shell
python manage.py migrate
```

### Create Admin Account

```shell
python manage.py createsuperuser
```

### Run server

```shell
python manage.py runserver | python manage.py runserver your_ip_addres:8000
```