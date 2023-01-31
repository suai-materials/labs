import requests

from Position import Position
# Запускаю конвертер режиссёров и актёров
from prepare import *
from bs4 import BeautifulSoup

GENERAL_URL = "https://www.mariinsky.ru"

# Сопаставление реальных людей к виртуальным
actors_dict = {}
directors_dict = {}
staff_dict = {}
performance_types = []
performance = []
duration_acts = [(90, 1), (120, 1), (180, 2), (60, 1), (240, 3), (300, 3), (360, 3)]

bs = BeautifulSoup(requests.get(GENERAL_URL + "/company/opera/management/").text, "html.parser")

staff_index = 0
for s in bs.findAll("p"):
    name = s.findNext("strong").text
    positions.append(Position(s.contents[-1].lstrip().title()))
    staff[staff_index].position_id = len(positions)
    staff_index += 1

positions.append(Position("Концертмейстер",
                          "Руководитель группы инструментов в симфоническом оркестре" + \
                          "(или ином оркестре: народных инструментов, духовом), " + \
                          "обычно наиболее опытный и/или одарённый исполнитель на соответствующем инструменте" + \
                          "в данном коллективе"))

for i in range(5, 15):
    staff[staff_index].position_id = len(positions)
    staff_index += 1

bs = BeautifulSoup(requests.get(GENERAL_URL + "/company/opera/coach/").text, "html.parser")

for s in bs.findAll("p"):
    name = s.findNext("strong").text
    positions.append(Position(s.contents[-1].lstrip().title()))
    staff[staff_index].position_id = len(positions)
    staff_index += 1

positions.append(Position("Врачи-фониатры", "Врачи, которые лечат голос"))

for i in range(1, 6):
    staff[staff_index].position_id = len(positions)
    staff_index += 1
staff = list(filter(lambda st: st.position_id != -1, staff))
print(positions)
input()

# .*\s–\s.*
# Год
year: int = 2021
# Номер сезона
season: int = 239
# Номер стартового месяца
start_month: int = 9
# Номер конечного месяца
end_month: int = 12
# Организация импорта постановок данных с сайта мариинского сайта
for i in range(start_month, end_month + 1):
    bs = BeautifulSoup(requests.get(GENERAL_URL + "/playbill/archive/",
                                    params={"season": season, "month": i, "year": year}).text, "html.parser")
    for row in bs.findAll("div", class_="day_row"):
        for perf_in_date in row.findAllNext("div", class_="spec_row"):
            print(perf_in_date.findNext("span", itemprop="summary").text)
