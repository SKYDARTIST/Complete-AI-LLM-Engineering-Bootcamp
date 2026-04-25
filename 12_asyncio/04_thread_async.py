import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):

    print(f"Checking stock for {item}...")

    time.sleep(3) #blocking operation

    print(f"Stock checked for {item}!")

    return f"{item} stock is available!"

async def main():
    loop = asyncio.get_event_loop()
    items = ["Milk", "Bread", "Eggs"]
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Bread")
    print(result)
    
asyncio.run(main())
