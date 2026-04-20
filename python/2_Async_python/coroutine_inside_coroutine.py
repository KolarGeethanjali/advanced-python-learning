import asyncio

#coroutine means specific function in python
async def process1():
    print("this is process1 first step")
    await asyncio.sleep(3) #there can be api call #await resumes the event loop
    result = await process2() # calling another coroutine inside this coroutine
    print("this is process1 second step")
    print(f"result of process2 is: {result}")

# here between these two steps coroutine doesnot work

async def process2():
    print("this is process2 first step")
    await asyncio.sleep(3) #there can be api call #await resumes the event loop
    print("this is process2 second step")
    return "process2 is done"

#Event loop1 begins
asyncio.run(process1()) # calling coroutine (this starts the eventloop)

