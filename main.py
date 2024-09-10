from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


app = FastAPI()

data_store = []

# Sample data to demonstrate GET call
@app.get("/api/data")
async def get_data():
    return JSONResponse(content=data_store)

# Sample data to demonstrate POST call
@app.post("/api/data")
async def post_data(request: Request):
    new_data = await request.json()
    data_store.append(new_data)
    return JSONResponse(content=new_data, status_code=201)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
