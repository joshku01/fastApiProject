from fastapi import APIRouter, HTTPException, Query, Path
from typing import Union, List
from pydantic import Required
from repository import schemas

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

dict_2 = dict(name="Plumbu", year=1985, director='test')

list_1 = ['Peter', 'Josh']


@router.get("/")
async def read_items(size: Union[str, None] = Query(default=Required, min_length=3)):  # 聲明參數,size參數 最小長度為3
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if size:
        results.update({"size": size})
    return fake_items_db


@router.get("/data/")
async def get_items(r: Union[List[str], None] = Query(default=None)):  # 可以使用多個值的方式
    query_items = {"r": r}
    return query_items


@router.get("/{item_id}")
async def read_item(
        item_id: int = Path(title="The ID of the item to get"),
        q: Union[str, None] = Query(default=None, alias="item_query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@router.put("/{item_id}", )
async def update_item(
        *,
        item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
        q: Union[str, None] = None,
        item: Union[schemas.Item, None] = None
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})
    return result
