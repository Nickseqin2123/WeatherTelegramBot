from selenium import webdriver
from bs4 import BeautifulSoup
from fake_headers import Headers
from googlesearch import search


def web(punct):
    try:
        url = search(f"Яндекс погода в {punct}", num_results=1).__next__()
    except Exception:
        return "SEARCH ERROR"
    else:
        headers = Headers().generate()
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument(f'User-Agent={headers["User-Agent"]}')
        options.add_argument(f'Accept={headers["Accept"]}')
        driver.get(url)
        # time.sleep(1)
        #html = driver.page_source
        with open("weather.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        driver.quit()
        # return html    


def pars_weath(message):
    from_web = web(message)
    try:
        with open("weather.html", encoding="utf-8") as f:
            from_web = f.read()
            
        soup = BeautifulSoup(from_web, "lxml")
        name = soup.find(class_="title").text
        temp_now = soup.find(class_="temp fact__temp fact__temp_size_s").text
        temp_like = soup.find(class_="term term_orient_h fact__feels-like").find(class_="temp").text
        time_now = soup.find(class_="time fact__time").text
        stat = soup.find(class_="link__condition day-anchor i-bem").text
        atmosphere = soup.find(class_="fact__props").find_all(class_="a11y-hidden")[-1].text.split()
        city_time = f"""{name}
{time_now}
{stat}
Температура воздуха: {temp_now} ℃
По ощущению: {temp_like} ℃
Атмосферное давление: {" ".join(atmosphere[:2])} мм.рт.ст.
{soup.find(class_="maps-widget-fact__title").text}
        """
        return city_time
    except Exception:
        return "ERROR"