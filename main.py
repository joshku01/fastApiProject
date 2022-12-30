from fastapi import FastAPI, Depends
from internal.member import LineLogin
from routers import user, item

from repository import models
from repository.database import engine

# import sqlalchemy

app = FastAPI()

models.Base.metadata.create_all(engine)

# print(sqlalchemy.__version__)
# 引入其他模塊的api router
app.include_router(user.router)
app.include_router(item.router)


@app.get("/")
async def root():
    login = LineLogin()
    login.login()
    return {"message": "Hello World"}

# if __name__ == "__main__":
#     uvicorn.run("__main__:app", host="0.0.0.0", port=8089, reload=True, workers=2, proxy_headers=True,
#                 forwarded_allow_ips='*')
