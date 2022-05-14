#!/bin/bash
DIR="$( cd "$( dirname "$0" )" && pwd )"
echo $DIR

cd $DIR

# ulimit -n 50000
nohup gunicorn --config=djangoProject/gunicorn_conf.py djangoProject.wsgi &> /dev/null &