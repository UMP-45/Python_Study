#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from redis.connection import ConnectionPool
from redis.client import Redis

def redis_conn_pool():
    redis_pool = ConnectionPool(host='localhost', port= 6379, db= 0)
    redis_conn = Redis(connection_pool= redis_pool)
    return redis_conn