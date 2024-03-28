from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="simple-store")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return "Hello world!"

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

 


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)