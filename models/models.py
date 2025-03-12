from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey


class Model(DeclarativeBase):
    ...
    

class Countries(Model):
    __tablename__ = 'countries'
    
    iso: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    
    regions = relationship('Regions', back_populates='countries', lazy='selectin')
    districts = relationship('Districts', back_populates='countries', lazy='selectin')
    cities = relationship('Districts', back_populates='countries', lazy='selectin')


class Regions(Model):
    __tablename__ = 'regions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.iso', ondelete='CASCADE'))
    
    name: Mapped[str] = mapped_column(String(100))
    
    countries = relationship('Countries', back_populates='regions', lazy='selectin')
    districts = relationship('Districts', back_populates='regions', lazy='selectin')
    

class Districts(Model):
    __tablename__ = 'districts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.iso', ondelete='CASCADE'))
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id', ondelete='CASCADE'))
    
    name: Mapped[str] = mapped_column(String(100))
    countries = relationship('Countries', back_populates='districts', lazy='selectin')
    regions = relationship('Regions', back_populates='districts', lazy='selectin')
    

class Сities(Model):
    __tablename__ = 'cities'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.iso', ondelete='CASCADE'))
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id', ondelete='CASCADE'))
    district_id: Mapped[int] = mapped_column(ForeignKey('districts.id', ondelete='CASCADE'), nullable=True)
    
    name: Mapped[str] = mapped_column(String(100))
    
    countries = relationship('Countries', back_populates='cities', lazy='selectin')
    districts = relationship('Regions', back_populates='cities', lazy='selectin')
    regions = relationship('Districts', back_populates='cities', lazy='selectin')