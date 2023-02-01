from dataclass_csv import DataclassWriter, DataclassReader
from datetime import datetime as dt
from typing import List

from Actor import Actor
from Director import Director
from Position import Position
from Scene import Scene
from Staff import Staff
from PerformanceType import PerformanceType

actors: List[Actor] = []
directors: List[Director] = []
scenes: List[Scene] = []
staff: List[Staff] = []
positions: List[Position] = []
perf_types: List[PerformanceType] = []

# Адаптирую придуманную информацию или информацию сгенерированную
# для Python, для её дополнения или изменения

with open("data_files/data_fio_a.txt", "r", encoding='utf-8') as fio_f:
    with open("data_files/data_date_a.txt", "r", encoding='utf-8') as date_f:
        for fio, date in zip(fio_f.readlines(), date_f.readlines()):
            actors.append(Actor(fio.split()[0], fio.split()[1], fio.split()[2].replace('\n', ''),
                                dt.strptime(date.replace('\n', ''), "%Y-%m-%d %H:%M:%S").date()))
    # with open("Артисты.csv", 'w', newline='', encoding='utf-8') as fw:
    #     DataclassWriter(fw, actors, Actor).write()

with open("data_files/data_fio_d.txt", "r", encoding='utf-8') as fio_f:
    with open("data_files/data_date_d.txt", "r", encoding='utf-8') as date_f:
        for fio, date in zip(fio_f.readlines(), date_f.readlines()):
            directors.append(Director(fio.split()[0], fio.split()[1], fio.split()[2].replace('\n', ''),
                                      dt.strptime(date.replace('\n', ''), "%Y-%m-%d %H:%M:%S").date()))
    # with open("Режиссёры.csv", 'w', newline='', encoding='utf-8') as fw:
    #     DataclassWriter(fw, directors, Director).write()

with open("data_files/scene.csv", 'r', encoding='utf-8') as scene_f:
    scenes = list(DataclassReader(scene_f, Scene))

with open("data_files/data_fio_p.txt", "r", encoding='utf-8') as fio_f:
    for fio in fio_f.readlines():
        staff.append(Staff(*fio.replace('\n', '').split()))


with open("data_files/performance_type.csv", "r", encoding='utf-8') as f:
    perf_types = list(DataclassReader(f, PerformanceType))