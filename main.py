from fastapi import FastAPI

from example.controllers.items import GetItemsController

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/example/items")
async def example_items():
    return {
        "example": [
            {"id": "1", "self": "/example/items/1"},
            {"id": "2", "self": "/example/items/2"},
        ]
    }


@app.get("/example/items/{item_id}")
async def read_item(item_id):
    item_controller = GetItemsController()
    return item_controller.get(item_id)
