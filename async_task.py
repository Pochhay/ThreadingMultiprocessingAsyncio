import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):
    print(f"Opening {filename}")
    async with aiofiles.open(filename, 'w') as f:
        for i in data:
            await f.write(f"{i} \n")
    print(f"Wrote to {filename} in {duration} seconds")
    await asyncio.sleep(duration)
    print(f"Finish writing in {filename}") 

async def run_async_tasks(data):
    files_to_write = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = []

    for file in (files_to_write):
        task = async_write_to_file(file, data, 10)
        tasks.append(task)

    await asyncio.gather(*tasks)