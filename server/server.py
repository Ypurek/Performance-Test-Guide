from fastapi import FastAPI
from contextlib import contextmanager
import asyncio
import random
import logging
import time

app = FastAPI(debug=True)
log = logging.getLogger("uvicorn")
log.setLevel('INFO')


# recursive solution done intentionally
async def fib(x: int) -> int:
    if type(x) is not int:
        return 0
    if 1 <= x <= 40:
        return await fib(x - 1) + await fib(x - 2)
    return 1


@contextmanager
def count_time():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    duration = round(end - start, 3)
    log.info(f'Operation done in -> {duration:6}')


@app.get('/')
async def fast():
    return 'hello world'


@app.get('/unstable')
async def unstable():
    probability = random.randint(1, 500)
    log.debug(f'probability -> {probability:3}')
    if probability <= 20:
        log.info('unstable sleep started')
        await asyncio.sleep(30)
        log.info('unstable sleep ended')
    return 'unstable response'


@app.get('/fibonacci')
async def fibonacci(number: int = 1):
    with count_time():
        result = await fib(number)
    return result


@app.get('/wait')
async def wait(sec: int = 0):
    await asyncio.sleep(sec)
    return f'{sec} sec waited'


@app.get('/sort')
async def sort(n: int = 10_000):
    with count_time():
        random.sample(population=range(n), k=n).sort()
    return f'sort of {n}-list done'
