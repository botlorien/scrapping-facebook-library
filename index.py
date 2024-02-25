from fastapi import FastAPI
import tasks as ts
from mangum import Mangum
app = FastAPI()

@app.get("/")
async def root():
    content = await ts.get_facebook_ads()
    return {"content": content}

handler = Mangum(app)