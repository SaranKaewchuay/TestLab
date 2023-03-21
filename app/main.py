from fastapi import FastAPI
from mangum import Mangum
from .tests.function import display_month

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/test")
def AAAA():
    input_number = input()
    try:
        try:
            input_number = int(input_number)
        except:
            input_number = float(input_number)

    except:
        input_number = str(input_number)

    result = display_month(input_number)
    print(result)



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/hello/{name}")
# def read_name(name: str = None):
#     return {"hello": name}


# @app.get("/test")
# def read_name():
#     return {"Hello": "World2"}


handler = Mangum(app)
