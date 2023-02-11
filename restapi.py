from fastapi import FastAPI
# from BasicGenerator import BasicGenerator

app = FastAPI()


@app.get("/gen/{name}/{number}")
async def root(name: str, number: int):
    """
    делаем запрос на генерацию ника
    """
    # b = BasicGenerator(number, name)
    return {"message": f'get {name}, {number}'}


@app.post("/gen")
async def root(name: str, number: int):
    return {"message": f'post {name}, {number}'}