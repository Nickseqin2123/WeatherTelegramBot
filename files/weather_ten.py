from fake_headers import Headers
from selenium import webdriver
from bs4 import BeautifulSoup
from googlesearch import search


def web(punct):
        header = Headers(
        browser="chrome",
        os="win",
        headers=True
    )
        try:
            sear = search(f"Яндекс погода в {punct} на 10 дней", num_results=2).__next__()
        except Exception:
            return "SEARCH ERROR"
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument(f"headers={header.generate()}")
        driver.get(sear)
        with open("weather_ten.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        #html = driver.page_source
        driver.quit()
        # return html
    

def week_weath(city):
    from_web = web(city)
    widgets = []
    try:
        with open("weather_ten.html", encoding="utf-8") as f:
            from_web = f.read()
        soup = BeautifulSoup(from_web, "lxml")
        all = soup.find_all(class_="forecast-briefly__day")
    except Exception as er:
        return "ERROR"
    
    for i in range(2, len(all) - 19):
        widgets.append(f"""День недели:{all[i].find(class_="forecast-briefly__name").text} Число: {all[i].find(class_="time forecast-briefly__date").text}
Температура днем/ночью: {all[i].find(class_="temp forecast-briefly__temp forecast-briefly__temp_day").text}℃  {all[i].find(class_="temp forecast-briefly__temp forecast-briefly__temp_night").text}℃
{all[i].find(class_="forecast-briefly__condition").text}
""")
    
    return "\n".join(widgets)
