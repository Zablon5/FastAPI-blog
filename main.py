from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Zerihun'}}

@app.get('/about')
def about():
    return {'about':'he is...'} 