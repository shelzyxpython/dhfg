# import asyncio
# import time
#
#
# async def async_func(task_no):
#     print('...start{task_no}')
#     await asyncio.sleep(3)
#     print('...end{task_no}')
#
#
# async def main():
#     task1 = asyncio.create_task(async_func('A'))
#     task2 = asyncio.create_task(async_func('B'))
#     task3 = asyncio.create_task(async_func('C'))
#     await asyncio.wait([task1, task2, task3])
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#
# def multiply(a, b):
#     return a * b

# import asyncio
#
#
# async def count(counter):
#     print(f'Количество записей в списке{len(counter)}')
#     while True:
#         await asyncio.sleep(1/1000)
#         counter.append(1)
#
#
# async def print_every_sec(counter):
#     while True:
#         await asyncio.sleep(1)
#         print(f'- 1 sec passed. Count = {len(counter)}')
#
#
# async def print_every_5sec():
#     while True:
#         await asyncio.sleep(1)
#         print(f'5 sec passed')
#
#
# async def print_every_10sec():
#     while True:
#         await asyncio.sleep(10)
#         print(f'10 sec passed')
#
#
# async def main():
#     counter = list()
#     # task1 = asyncio.create_task(count(counter))
#     # task2 = asyncio.create_task(print_every_sec(counter))
#     # task3 = asyncio.create_task(print_every_5sec())
#     # task4 = asyncio.create_task(print_every_10sec())
#     # await asyncio.wait([task1, task2, task3, task4])
#
#     task_list = [
#         count(counter),
#         print_every_sec(counter),
#         print_every_5sec(),
#         print_every_10sec()
#     ]
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())

# import httpx
# import asyncio
#
#
# async def Plus(a,b):
#     print('складывание началось')
#     await asyncio.sleep(5)
#     print('результат суммы', a+b)
#     return a**2
#
# async def kvadrat(a):
#     print()
#
# async def main():
#     task1=asyncio.create_task(Plus(2,4))
#     task2=asyncio.create_task(kvadrat(4))

import asyncio

async def calls():
    print(f'секретарь отвечает на звонки')
    await asyncio.sleep(1)


async def takes():
    await asyncio.sleep(2)
    print(f'секретарь принимает людей')


async def airlines():
    await asyncio.sleep(3)
    print(f'бронирует билеты')


async def graphics():
    await asyncio.sleep(4)
    print(f'редактирует график работы')


async def docks():
    await asyncio.sleep(5)
    print(f'заполняет документы')


async def main():
    task_list = [
        calls(),
        takes(),
        airlines(),
        calls(),
        graphics(),
        docks()
    ]
    await asyncio.gather(*task_list)

asyncio.run(main())