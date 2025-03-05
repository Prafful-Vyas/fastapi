from fastapi import FastAPI

app = FastAPI()

# request GET method url: "/"
# in case of same path for two functions, first one get chosen

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts():
    return {"message": "successfully created posts"}