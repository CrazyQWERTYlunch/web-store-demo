from fastapi import FastAPI, Request, Depends 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from catalog.router import catalog_router
###########################
## Router's and main app ##
###########################

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(title="simple-store",lifespan=lifespan) # lifespan=lifespan
app.include_router(catalog_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/home/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login_register.html")
 



if __name__ == "__main__":
    uvicorn.run(app="main:app",
                reload=True,
                port=8000)