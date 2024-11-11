from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
	return { "message": "Hello Jack! Newer give up!" }