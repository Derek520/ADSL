#!/bin/sh

ps -ef|grep -v grep|grep api.py|while read u p o
do
    kill -9 $p
done

while true
do

    ps -fe|grep api.py |grep -v grep
    if [ $? -ne 0 ]
    then
        echo 'start process'
        kill `lsof -t -i:5000`
        adsl-stop
        adsl-start
        python run.py
        python api.py
    else
        echo "runing....."

        sleep 1
    fi
done
#####