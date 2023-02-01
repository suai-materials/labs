import datetime
import random
import re
import os

import requests

from ActorDate import ActorDate
from Author import Author
from AuthorPerfomance import AuthorPerformance
from Performance import Performance
from Position import Position
from Role import Role
from TimeTable import TimeTable
# Запускаю конвертер режиссёров и актёров
from prepare import *
from bs4 import BeautifulSoup

GENERAL_URL = "https://www.mariinsky.ru"

# Сопоставление сцен
MAIIRINSKY_TO_PANKOVSKY = {
    "Мариинский театр": 1,
    "Концертный зал": 3,
    "Мариинский-2 ": 2
}

# Сопаставление реальных людей к виртуальным
actors_dict = {}
directors_dict = {}
staff_dict = {}

# Заполняемые списки
performances: List[Performance] = []
authors: List[Author] = []
authors_perf: List[AuthorPerformance] = []
timetable: List[TimeTable] = []
roles: List[Role] = []
actors_date: List[ActorDate] = []

duration_acts = [(90, 1), (120, 1), (180, 2), (60, 1), (240, 3), (300, 3), (360, 3)]

# Получение профессий и выдача их случайным людям

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
# print(positions)
# input()

# .*\s–\s.*
# Год
year: int = 2021
# Номер сезона
season: int = 239
# Номер стартового месяца
start_month: int = 9
# Номер конечного месяца
end_month: int = 9
# Организация импорта постановок данных с сайта мариинского сайта
for i in range(start_month, end_month + 1):
    bs = BeautifulSoup(requests.get(GENERAL_URL + "/playbill/archive/",
                                    params={"season": season, "month": i, "year": year}).text, "html.parser")
    for row in bs.findAll("div", class_="day_row"):
        for perf_in_date in row.findAllNext("div", class_="spec_row"):
            comment = perf_in_date.findNext("div", class_="status").text

            start_time = datetime.datetime.strptime(perf_in_date.findNext("time")["datetime"],
                                                    "%Y-%m-%dT%H:%M:%S+03:00")
            try:
                scene_id = MAIIRINSKY_TO_PANKOVSKY[perf_in_date.findNext("span", itemprop="location").text]
            except KeyError:
                scene_id = 3
            name = perf_in_date.findNext("span", itemprop="summary").text
            is_dubl = False
            for perf in performances:
                if perf.name == name:
                    is_dubl = True
                    perf_pos = performances.index(perf) + 1
                    timetable.append(TimeTable(perf_pos, scene_id, start_time, comment))
                    good_roles = list(filter(lambda r: r.performance_id == perf_pos, roles))
                    if good_roles == 0:
                        roles.append(Role(f"Ведущий {name}", perf_pos))
                        actors_date.append(
                            ActorDate(len(timetable), actors.index(random.choice(actors)) + 1, len(roles)))
                    else:
                        for role, actor in zip(good_roles, random.sample(actors, len(good_roles))):
                            actors_date.append(
                                ActorDate(len(timetable), actors.index(actor) + 1, roles.index(role) + 1))
                    break
            if is_dubl:
                continue

            description = perf_in_date.findNext("div", class_="descr").text
            author_id: int = -1
            # Ищем авторов произведения с помощью регистров
            for el in re.findall(
                    r'(балет|опера|оперетта)\s([А-Я]{1}[а-я]+\s[а-яА-Я-]+\s[А-Я]{1}[а-я]+|[А-Я]{1}[а-я]+\s[А-Я]{1}[а-я]+-[А-Я]{1}[а-я]+|[А-Я]{1}[а-я]+\s[А-Я]{1}[а-я]+)',
                    description):
                splitted = el[1].split()
                first_name, last_name = splitted if len(splitted) == 2 else splitted[:2]
                second_name = "" if len(splitted) == 2 else splitted[2]
                author_found = False
                for author in authors:
                    if author.last_name == author.last_name and author.first_name == first_name and author.second_name == second_name:
                        author_id = authors.index(author) + 1
                        author_found = True
                        break
                if not author_found:
                    authors.append(Author(last_name, first_name, second_name))
                    author_id = len(authors)

            founded = False
            perf_type_id: int = -1
            for perf_type in perf_types:
                if perf_type.name.lower() in description:
                    perf_type_id = perf_type.id
                    founded = True
            if not founded:
                perf_type_id = perf_types[-1].id

            duration = random.choice(duration_acts)
            performances.append(Performance(name, perf_type_id, duration[1], duration[0]))
            authors_perf.append(AuthorPerformance(author_id, len(performances)))
            timetable.append(TimeTable(len(performances), scene_id, start_time, comment))
            page_url = perf_in_date.findNext("a", itemprop="url")["href"]
            # Получаем большую информацию о представлении
            try:
                bs_two = BeautifulSoup(requests.get(GENERAL_URL + page_url).text, "html.parser")
                all_info = bs_two.findAll("div", class_="sostav")
                # Ищем роли
                for el in re.findall(r"(.+?)\s–\s([А-Я][а-я]+\s[А-Я][а-яё]+)", all_info[0].text):
                    if el[0] == "Дирижёр":
                        continue
                    roles.append(Role(el[0].lstrip(), len(performances)))
            except IndexError:
                pass
            good_roles = list(filter(lambda r: r.performance_id == len(performances), roles))
            # Если ролей не найдено
            if good_roles == 0:
                roles.append(Role(f"Ведущий {name}", len(performances)))
                actors_date.append(ActorDate(len(timetable), actors.index(random.choice(actors)) + 1, len(roles)))
            else:
                for role, actor in zip(good_roles, random.sample(actors, len(good_roles))):
                    actors_date.append(ActorDate(len(timetable), actors.index(actor) + 1, roles.index(role) + 1))

os.chdir("/result")

with open("artists.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, actors, Actor)

with open("directors.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, directors, Director)

with open("authors.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, authors, Author)

with open("auth_perf.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, authors_perf, AuthorPerformance)

with open("staff_position.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, positions, Position)

with open("staff.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, staff, Staff)

with open("performance.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, performances, Performance)

with open("role.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, roles, Role)

with open("timetable.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, timetable, TimeTable)

with open("actors_date.csv", "w", encoding="utf-8") as f:
    DataclassWriter(f, actors_date, ActorDate)