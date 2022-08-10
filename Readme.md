# Materials for performance testing demo

## Server
Server to be tested. Written in Python, using [FastAPI](https://fastapi.tiangolo.com/) framework
and [Uvicorn](https://www.uvicorn.org/) as ASGI web server implementation. It is async so requests don't block each other.

In my [previous attempt](https://github.com/Ypurek/performance-sample) I was using 
[Flask](https://flask.palletsprojects.com/) and [gunicorn](https://gunicorn.org/), but services are blocked 
during `time.sleep()` operation

### Endpoints:
 - `/` just hello world, no logic, fast response
 - `/unstable` fast response, no logic, with probability 4% waits 30 sec before respond
 - `/fibonacci` the most 'heavy', calculates n-member of fibonacci sequence. Implemented with recursion to make it heavier. ⚠️works well up to 40th member
 - `/wait?sec=0` waits n seconds before response. Set by query parameter. 0 by default
 - `/sort?n=10000` generates list of random integers, then sort it. Expected to be another heavy operation

## Tests
### Locust
#### [locustfile1.py](locustfile1.py)
1st tutorial, no real testing, the only task active for `/unstable` endpoint to show how
test started and going. What metrics can be collected