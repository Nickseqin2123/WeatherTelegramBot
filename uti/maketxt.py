async def txt_get(data: list[dict]):
    if isinstance(data, list):
        datas = []
        
        for ind, obj in enumerate(data, start=1):
            datas.append(f'{ind}. `{obj['name']}`')
        
        return '\n'.join(datas)
    
    return 'Не существует такой страницы'