# -*- coding: utf-8 -*-
import socket,fcntl,struct
from redis import StrictRedis
from config import *

class AutoProxy(object):
    def __init__(self):
        self.redis_store = StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB)

    def task(self):
        try:
            ip = self.get_local_ip('ppp0')
            self.redis_store.hset(KEY,FIELD,ip)
        except Exception as e:
            print e

    def get_local_ip(self,ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
        ret = socket.inet_ntoa(inet[20:24])
        return ret


if __name__ == '__main__':
    ap = AutoProxy()
    ap.task()