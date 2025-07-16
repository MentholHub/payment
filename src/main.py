from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """
    Just documentation
    """
    return {"key": "value"}
