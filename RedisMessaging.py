# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:58:06 2020

@author: Himanshu.Manjarawala
"""

# step 1: import redis-py client package
import redis


# step 2: define our connection information for redis
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def hello_redis():
    """Example Hello Redis Program"""
    
    # step 3: create the redis connection object
    try:
        
        r = redis.StrictRedis(
                host=redis_host,
                port=redis_port,
                password=redis_password,
                decode_responses=True
                )
        
        # step 4: set hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")
        
        # step 5: Retrive the hello message from Redis
        msg = r.get("msg:hello")
        
        print(msg)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()