import time
import redis

from flask import Flask

print(__name__)

app = Flask(__name__)

cache = redis.StrictRedis(host='localhost', port=6379)

def get_hit_count():

    retries = 5

    while True:

        try:
            if not cache.exists('hits'):                
                cache.set('hits', 0)
            cache.incr('hits')
            count = (cache.get('hits')).decode('utf-8')
            return count

        except redis.exceptions.ConnectionError as exc:

            if retries == 0:

                raise exc

            retries -= 1

            time.sleep(0.5)


@app.route('/')
def hello():

    count = get_hit_count()

    return 'Hello World! I have been seen {} times.'.format(count)

if __name__ == "__main__":
    print('Entered')
    app.run(host = '0.0.0.0',port=8000)
    print('Exited')