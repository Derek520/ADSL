# -*- coding: utf-8 -*-

from flask import Flask
import commands
from redis import StrictRedis
from config import *

app = Flask(__name__)


@app.route('/proxy')
def hello_world():
    rq = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB)
    rq.hdel(KEY,FIELD)
    commands.getoutput('pkill -f api.py')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
