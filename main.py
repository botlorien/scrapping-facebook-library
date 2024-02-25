from fastapi import FastAPI
import asyncio
from pyppeteer import launch

app = FastAPI()

async def fetch_with_pyppeteer():
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'])
    page = await browser.newPage()
    await page.goto('http://example.com')
    content = await page.content()
    await browser.close()
    return content

@app.get("/")
async def root():
    content = await fetch_with_pyppeteer()
    return {"content": content}
