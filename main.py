from datetime import datetime
from typing import List

from fastapi import FastAPI, status
from starlette.responses import Response
from pydantic import BaseModel

app = FastAPI()

information_db = []

class Information(BaseModel):
    author : str
    title : str
    content : str
    creation_datetime : datetime


@app.get("/ping")
def read_ping():
    return Response("pong", status_code=200)

@app.get("/home")
def read_home():
    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("not_found.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")

@app.post("/information", status_code=status.HTTP_201_CREATED)
def add_information(new_information : List[Information]):
    for information in new_information:
        information_db.append(information)
    return information_db

@app.get("/information")
def get_information():
    return information_db





