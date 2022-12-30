from fastapi import Header, HTTPException
from secrets import compare_digest


async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if compare_digest(token, "1234567890"):
        raise HTTPException(status_code=400, detail="No given token provided")
