from fastapi import FastAPI
from mangum import Mangum
from .tests.calculate_grade import calculate_grade

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/calculate_grade/{score}')
def calculate_grade_api(score:int):
    grade = calculate_grade(score)
    return grade

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/hello/{name}")
def read_name(name: str = None):
    return {"hello": name}


handler = Mangum(app)
