from pydantic import BaseModel, ConfigDict, condecimal
from typing import Annotated, Optional

#############################################
##      pydantic schemas  for catalog      ##
#############################################

# Pydantic модель для входящих данных POST запроса (добавление категории)
class SCategoryCreate(BaseModel):
    name: str
    slug: str | None = None
    # Можно прокинуть валидаторы на модель, через @validator("столбец")

# Pydantic модель для выходящих данных GET запроса (получение информации о категории)

class SProductCreate(BaseModel):
    name: str
    slug: str | None = None
    quantity: int = 0
    price: condecimal(ge=0) = 100.0
    category_id: int | None = None


class SCategory(SCategoryCreate):
    id: int
    products: list["SProduct"]

    model_config = ConfigDict(from_attributes=True)

class SCategoryId(BaseModel): # Модель для ответа при добавлении
    ok: bool = True
    category_id: int

class SProduct(SProductCreate):
    id: int
    # category: "SCategory" # Можно включить но надо будет решать проблему с рекурсией

    model_config = ConfigDict(from_attributes=True)



