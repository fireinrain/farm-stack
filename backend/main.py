import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get('/')
def read_root():
    return {"ping": "ping"}


@app.get('/api/todo{id}')
async def get_todo_by_id(id: int):
    return 1


@app.post('/api/todo')
async def post_todo(data: dict):
    return 1


@app.put('/api/todo')
async def put_todo(id: int, data: dict):
    return 1


@app.delete('/api/todo{id}')
async def delete_todo(id: int):
    return 1


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
