from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

#######################################
##      ORM models  for catalog      ##
#######################################

class CategoryOrm(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    slug: Mapped[str | None]
    products: Mapped[list["ProductOrm"]] = relationship(
        back_populates="category",
        lazy="selectin"
    )

class ProductOrm(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    slug: Mapped[str] = mapped_column(nullable=True)
    quantity: Mapped[int] = 0
    price: Mapped[float] = 100.0
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="SET NULL"), nullable=True)
    category: Mapped["CategoryOrm"] = relationship(
        back_populates="products",
        lazy="joined"
    )