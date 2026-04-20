import asyncio

async def process1():
    print("this is process1 first step")
    await asyncio.sleep(3) 
    print("this is process1 second step")

# here between these two steps coroutine doesnot work

async def process2():
    print("this is process2 first step")
    await asyncio.sleep(6)
    print("this is process2 second step")


# def main():
#     asyncio.run(process1())
#     asyncio.run(process2())

# main()

async def main(): 
    # await process1() # we use await when calling one coutine with in another coroutine
    # await process2()

    tasks = await asyncio.gather(process1(), process2()) # this is used to run multiple coroutines at same time so that eventloop works between coroutines and we can save time instead of waiting for one coroutine to complete and then starting another coroutine.
    print("main completed")

asyncio.run(main())

#the result order changes when comapred to calling one coroutine inside another just notice

