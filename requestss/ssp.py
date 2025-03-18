import asyncio
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from models.models import Countries, Regions
from .man import cfg


async def add_country(iso, name):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = insert(Countries).values(iso=iso, name=name)
                
            await session.execute(query)
            await session.commit()
    finally:
        await cfg.engine.dispose()
    
    return 'ok'


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


async def add_region(idd, country_id, name):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = insert(Regions).values(id=idd, country_id=country_id, name=name)
                
            await session.execute(query)
            await session.commit()
    finally:
        await cfg.engine.dispose()


asyncio.run(get_country('RU'))