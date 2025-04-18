import itertools


async def paginate(iterable, page_size):
    it = iter(iterable)
    pages = {}
    page_number = 1

    while True:
        chunk = list(itertools.islice(it, page_size))
        if not chunk:
            break
        pages[page_number] = chunk
        page_number += 1

    return pages