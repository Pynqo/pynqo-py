import os
from dotenv import load_dotenv
from pynqo import PynqoClient

load_dotenv()
client = PynqoClient(os.getenv("PYNQO_TOKEN"), "http://localhost:5051/")

keywords = client.guilds.get("545329817927811073")

print(keywords)