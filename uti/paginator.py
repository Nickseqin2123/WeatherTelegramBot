import itertools


async def paginator(data: list[tuple], page_size: int):
    pages = {}
    page_number = 1
    it = iter(data)
 
    while True:
        chunk = list(itertools.islice(it, page_size))
        if not chunk:
            break
        
        pages[page_number] = chunk
        page_number += 1
 
    return pages