from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy import insert
from models.config import cfg
from models.models import Puncts


async def add_user(user_id: int, lan: float, lon: float):
    session = async_sessionmaker(cfg.engine)
    
    try:
        async with session() as session:
            query = insert(Puncts).values(user_id=user_id, latitude=lan, longitude=lon)
            await session.execute(query)
            await session.commit()
            
    finally:
        await cfg.engine.dispose()
    
    return 'Добавление прошло успешно'