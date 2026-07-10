from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Menta Health AI backend is Running"
    }