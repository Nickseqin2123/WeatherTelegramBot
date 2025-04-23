from bs4 import BeautifulSoup


async def parser(html: str):
    bs = BeautifulSoup(html, 'lxml')

    main_content = bs.find(class_='content__top')

    if main_content is None:
        return 'Не удалось получить ответ от сервера. Попробуйте позже или напишите в тех.поддержку.'
    
    on_title = main_content.find(class_='fact__title')
    punct_name = on_title.find(class_='title title_level_1 header-title__title').text

    yesterday = on_title.find(class_='fact__time-yesterday-wrap')
    time = yesterday.find(class_='time fact__time').text
    temp = yesterday.find(class_='term__value').text

    fact_wrap = main_content.find(class_='fact__temp-wrap')
    temp = fact_wrap.find('span').text

    full_fact = fact_wrap.find(class_='link__feelings fact__feelings')
    up_fact = full_fact.find(class_='link__condition day-anchor i-bem').text
    term_where_fact = full_fact.find(class_='term term_orient_h fact__feels-like').find(class_='temp').text

    prognoz = main_content.find(class_='maps-widget-nowcast card content__brief')
    inner = prognoz.find(class_='maps-widget-fact maps-widget-nowcast__inner')
    prohnoz_full = inner.find('p', 'maps-widget-fact__title').text
    
    return f'''{punct_name}
{time}Вчера в это время {temp}

Температура: {temp}
{up_fact}
Ощущается как {term_where_fact}

{prohnoz_full}'''