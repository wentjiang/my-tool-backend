# my-tool-backend

#you can use pipenv to manager the python package
create virtual env
>pipenv shell

show which env is using
>which python


## Init Loacl ENV

### install pipenv & virtualenv
```
pip install --user pipenv
pip install virtualenv
```

### init virtualenv
```shell script
cd /project/dir
virtualenv venv
source ./venv/bin/activate
```

### install requirements
```shell script
pip install -r requirements.txt
```

### Put the installed package into requirements.txt
```shell script
pip freeze > requirements.txt
```

### build docker image

```
./scripts/build.sh
```

### start docker image

```
docker run --rm -p 5001:5001 wentjiang/my-tool-backend
```

### local run

```
python application.py 
```