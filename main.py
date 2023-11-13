from fastapi import FastAPI,File,UploadFile,Request,Form


app = FastAPI()

@app.get("/")
def homepage(request:Request):
    return {"Message From HomePage":"Hello World"}


@app.post("/index-document")
async def indexing_document(document: UploadFile = File(...)):
    return {"filename": document.filename}


