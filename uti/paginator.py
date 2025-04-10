import itertools


def paginate(iterable, page_size):
    it = iter(iterable)
    slicer = lambda: list(itertools.islice(it, page_size))
    
    return iter(slicer, [])