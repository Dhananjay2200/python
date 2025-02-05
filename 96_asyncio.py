import time
import asyncio
import requests

async def func1():

    print("func1")
    url = "https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    open("1.jpg","wb").write(response.content)
async def func2():

    print("func2")
    url = "https://images.pexels.com/photos/1402787/pexels-photo-1402787.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    open("2.jpg","wb").write(response.content)
async def func3():

    print("func3")
    url = "https://images.pexels.com/photos/1624496/pexels-photo-1624496.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    open("3.jpg","wb").write(response.content)

async def main():
    # await func1()
    # await func2()
    # await func3()
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),    )
    print(L)

asyncio.run(main())