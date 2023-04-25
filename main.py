from fastapi import FastAPI
import uvicorn
app=FastAPI()


@app.get("/home")
def home():

    return {"print":"hello world"}
@app.get("/about")
def about():

    return {"print":"hello"}

if __name__=="__main__":

    uvicorn.run(app,port=5000)
