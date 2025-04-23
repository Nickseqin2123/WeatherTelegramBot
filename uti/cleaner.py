import asyncio
import time


users_last_clik = {}
CLEAR_INETRVAL = 5
PEOPLE_TTL = 15


async def cleaner_dat():
    while True:
        await asyncio.sleep(CLEAR_INETRVAL)
        current_time = time.time()
        to_delete = [uid for uid, time_user in users_last_clik.items() if current_time - time_user >= PEOPLE_TTL]
        
        for uid in to_delete:
            del users_last_clik[uid]
        
        print(f'Очистка словаря с кликами. Очищено: {len(to_delete)}')