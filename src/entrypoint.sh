#!/bin/bash

if [ $1 = "shell_plus" ]
then
    exec python manage.py shell_plus
elif [ $1 = "runtests" ]
then
    exec echo 'runtest process'
elif [ $1 = "run" ]
then
    exec  streamlit run stream/moviechat.py --server.port=8501 --server.address=0.0.0.0
else
    #exec pipenv run $@
    exec $@
fi