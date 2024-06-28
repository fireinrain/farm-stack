import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo

)
from model import Todo

app = FastAPI()

# origins = ['http://localhost:3000']
# 请求跨域设置
origins = ['*']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get('/')
def read_root():
    return {"ping": "ping"}


@app.get('/api/todo', response_model=list)
async def get_todos():
    response = await fetch_all_todos()
    return response


@app.get('/api/todo/{title}', response_model=Todo)
async def get_todo_by_id(title: str):
    response = await fetch_one_todo(title)
    if not response:
        raise HTTPException(404, f"there is no TODO item with this title: {title}")

    return response


@app.post('/api/todo', response_model=Todo)
async def post_todo(data: Todo):
    data_dict = data.dict()
    response = await create_todo(data_dict)
    return response


@app.put('/api/todo/{title}', response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if not response:
        raise HTTPException(404, f"there is no TODO item with this title: {title}")
    return response


@app.delete('/api/todo/{title}')
async def delete_todo(title: str):
    response = await remove_todo(title)
    if not response:
        raise HTTPException(404, f"there is no TODO item with this title: {title}")
    return "remove todo item success!"


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
