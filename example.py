import os
import asyncio
from dotenv import load_dotenv
from pynqo import PynqoClient

async def main():
    load_dotenv()
    client = PynqoClient(os.getenv("PYNQO_TOKEN"), "http://localhost:5051/")
    
    keywords = await client.categories.list()
    print(keywords)

if __name__ == "__main__":
    asyncio.run(main())
