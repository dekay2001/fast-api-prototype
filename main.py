from fastapi import FastAPI

from dan.controllers.items import GetItemsController

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/dan/items")
async def dan_items():
    return {
        "dan": [
            {"id": "1", "self": "/dan/items/1"},
            {"id": "2", "self": "/dan/items/2"},
        ]
    }


@app.get("/dan/items/{item_id}")
async def read_item(item_id):
    item_controller = GetItemsController()
    return item_controller.get(item_id)

