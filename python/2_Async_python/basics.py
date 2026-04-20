import asyncio

#coroutine means specific function in python
async def process1():
    print("this is process1 first step")
    await asyncio.sleep(3) #there can be api call #await resumes the event loop
    print("this is process1 second step")

# here between these two steps coroutine doesnot work

async def process2():
    print("this is process2 first step")
    await asyncio.sleep(3) #there can be api call #await resumes the event loop
    print("this is process2 second step")

#Event loop1 begins
asyncio.run(process1()) # calling coroutine (this starts the eventloop)

#Event loop2 begins
asyncio.run(process2())

#calling coroutine inside another coroutine in next chap
