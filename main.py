import time

from fastapi import FastAPI, Depends
from internal.member import LineLogin, Person, TwitterLogin
from routers import user, item

from repository import models
from repository.database import engine
import json
from internal.lamb import Lambda

# import sqlalchemy

app = FastAPI()


def create_table():
    models.Base.metadata.create_all(engine)


# print(sqlalchemy.__version__)
# 引入其他模塊的api router
app.include_router(user.router)
app.include_router(item.router)


@app.get("/")
async def root():
    login = LineLogin()
    login.login()
    twitter_login = TwitterLogin()
    twitter_login.accelerate()
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))

    numbers = [x * 3 for x in range(10) if x > 4]  # lambda匿名函式
    print(numbers)
    numbers2 = [43, 12, 42, 68, 90]
    for i in numbers2:
        print(f'{i},')
        print(time.time())
    result = list(map(lambda x: x * 2, numbers2))
    result2 = [num * 2 for num in numbers2]
    print(result)
    print(result2)
    result3 = filter(lambda x: x > 10, numbers2)
    print(result3)
    x = [1, "tets", "sets"]
    json.dumps(x)
    person = Person('Josh', 'Ku', 'gin')
    print(person._Person__type)


    Lambda.title(None)

    return {"message": "Hello World"}


# if __name__ == "__main__":
#     create_table()
#     uvicorn.run("__main__:app", host="0.0.0.0", port=8089, reload=True, workers=2, proxy_headers=True,
#                 forwarded_allow_ips='*')
