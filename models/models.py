from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Float, Integer, UniqueConstraint


class Model(DeclarativeBase):
    ...


class Puncts(Model):
    __tablename__ = 'puncts'
    
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    
    __table_args__ = (
        UniqueConstraint('user_id', 'latitude', 'longitude', name='punct_combination'), # Комбинация user_id punct_name, будет уникальной
    )