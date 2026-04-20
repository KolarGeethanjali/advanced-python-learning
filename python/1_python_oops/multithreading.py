import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ['orders', 'customers', 'products']

def my_func(i):

    wait = random.randint(1,5) #wait = 3
    time.sleep(wait)
    print(f"Im {i} i took {wait} seconds")

# for i in tables:
#     my_func(i)

with ThreadPoolExecutor(max_workers=len(tables)) as executer:
    
    futures = executer.map(my_func,tables) #method 1

    # for i in tables:                     #method 2
    #     future = executer.submit(my_func,i)

# submit() when building robust ETL jobs
# map() for simple parallel API calls
# submit() = You manage each task manually

#map create futures parallelly, submit create futures individually