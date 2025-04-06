import asyncio
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from models.models import Countries, Regions, Districts
from .man import cfg


async def get_country(iso):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = select(Countries).filter(Countries.iso == iso)
                
            data = await session.execute(query)
            parsed = data.scalar_one_or_none()
            
            return parsed
    finally:
        await cfg.engine.dispose()
    

async def get_counties():
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = select(Countries)
                
            data = await session.execute(query)
            parsed = data.all()
            
            return parsed
    finally:
        await cfg.engine.dispose()


async def add_rayon(country_id, region_id, name):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = insert(Districts).values(country_id=country_id, region_id=region_id, name=name)
            await session.execute(query)
            await session.commit()
            
    finally:
        await cfg.engine.dispose()