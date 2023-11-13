from fastapi import FastAPI,Request


app = FastAPI()

@app.get("/")
def homepage(request:Request):
    return {"Message From HomePage":"Hello World"}




