import os
from fastapi import FastAPI
from dotenv import load_dotenv
from typing import List
from mcp.tools import get_tools, Tool

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/mcp/tools", response_model=List[Tool])
def list_tools():
    return get_tools()

