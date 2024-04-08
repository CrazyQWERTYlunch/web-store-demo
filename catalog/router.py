from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from repository import CategoryRepository
from typing import Annotated
from catalog.schemas import SCategoryCreate, SCategory, SCategoryId, SProductCreate, SProduct

#########################
## Route's for catalog ##
#########################

catalog_router = APIRouter(
    prefix="/catalog",
    tags=["Каталог"]
    )

templates = Jinja2Templates(directory="templates")

@catalog_router.get("/", response_class=HTMLResponse)
async def catalog(request: Request):
    return templates.TemplateResponse(request=request, name="catalog.html")

@catalog_router.get("/category/")
async def get_categories() -> list[SCategory]:
    categories = await CategoryRepository.view_category()
    return categories


@catalog_router.post("/category/add/") # В дальнейшем добавить возврат в виде модели response_model=SCategory
async def add_category(body: Annotated[SCategoryCreate, Depends()]) -> SCategoryId: 
    category_id = await CategoryRepository.add_one(body)
    return SCategoryId(ok=True, category_id=category_id)


@catalog_router.get("/product")
async def get_products() -> list[SProduct]:
    products = await CategoryRepository.view_products()
    return products

@catalog_router.post("/product/add")
async def add_product(body: Annotated[SProductCreate, Depends()]) -> dict[bool,int]:
    product_id = await CategoryRepository.add_product(body)
    return {"ok": True, "data": product_id}


