from sqlalchemy import select
from database import new_session

from catalog.models import CategoryOrm, ProductOrm
from catalog.schemas import SCategoryCreate, SCategory,SCategoryId, SProductCreate, SProduct

class CategoryRepository:

    @classmethod
    async def add_one(cls, category: SCategoryCreate) -> int:
        async with new_session() as session:
            category_dict = category.model_dump()
            new_category = CategoryOrm(**category_dict)
            session.add(new_category)
            await session.flush()
            new_category_id = new_category.id # очищается после комита потому пока извлекаем здесь
            await session.commit()
            return new_category_id
        
    @classmethod
    async def view_category(cls) -> list[SCategory]:
        async with new_session() as session:
            query = select(CategoryOrm)
            result = await session.execute(query)
            category_models = result.scalars().all()
            category_schemas = [SCategory.model_validate(category) for category in category_models]
            return category_schemas
        
    @classmethod
    async def add_product(cls, product: SProductCreate) -> int:
        async with new_session() as session:
            new_product = ProductOrm(**product.model_dump())
            session.add(new_product)            
            await session.flush()
            new_product_id = new_product.id
            await session.commit()
            return new_product_id
        
    @classmethod
    async def view_products(cls) -> list[SProduct]:
        async with new_session() as session:
            query = select(ProductOrm)
            result = await session.execute(query)
            product_models = result.scalars().all()
            product_schemas = [SProduct.model_validate(product) for product in product_models]
            return product_schemas