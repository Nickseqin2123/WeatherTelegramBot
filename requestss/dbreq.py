import asyncio

from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy import insert, select
from models.config import cfg
from models.models import Puncts


async def add_user(user_id: int, name: str, lat: float, lon: float):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = insert(Puncts).values(user_id=user_id, name=name, latitude=lat, longitude=lon)
            
            await session.execute(query)
            await session.commit()
    except Exception as er:
        print(er)
        return 'Произошла ошибка. Попробуйте /start или напишите в тех.поддержку'
    finally:
        await cfg.engine.dispose()
    
    return 'Добавление пункта прошло успешно'


async def get_puncts(user_id: int):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = select(Puncts).filter(Puncts.user_id == user_id)
            resp = await session.execute(query)
            scls = resp.scalars().all()
            
            if scls == []:
                return 'У вас не добавлены пункты. Добавьте их в меню регистрации'
            
            return scls
    except Exception as er:
        return er
    finally:
        await cfg.engine.dispose()