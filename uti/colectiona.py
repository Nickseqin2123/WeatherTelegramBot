async def colect(collecti: list[dict]):
    colct = []
    
    for i in collecti:
        colct.append({'id': i['id'], 'name': i['name'], 'type': i['type']})
    
    return colct