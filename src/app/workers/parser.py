import os
import time
from datetime import datetime
import re
from typing import List

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel


class PeriodDate(BaseModel):
    start_date: datetime
    end_date: datetime


class Link(BaseModel):
    url: str


class Schedule(BaseModel):
    course_code: int
    date: PeriodDate
    page_link: str


class ScheduleParser:
    def __init__(self):
        self.schedule_page = "http://eetk.ru/78-2/82-2/88-2/"

    def _get_page(self):
        r = requests.get(self.schedule_page)
        return r.text

    def parse_schedule_page(self) -> List[Schedule]:
        print("Parsing schedule page...")
        page = self._get_page()
        schedules_result = []
        course_added = []
        dates = []
        soup = BeautifulSoup(page, "html.parser")
        all_schedules = soup.find_all("td", class_="column-1")
        all_h3 = soup.find_all("h3")
        for h3 in all_h3:
            schedule_date = h3.find_all("strong")
            schedule_data = ""
            for schedule in schedule_date:
                schedule_data = schedule_data + schedule.text
            match = re.findall(r'\d{2}.\d{2}.\d{4}', schedule_data)
            result_date = []
            for date_str in match:
                date = datetime.strptime(date_str, '%d.%m.%Y').date()
                # print(date)
                result_date.append(date)
            if len(result_date) == 2:
                dates.append(PeriodDate(start_date=result_date[0], end_date=result_date[1]))
        for schedule in all_schedules:
            founded_schedule = schedule.find("a")
            link_rasp = founded_schedule["href"]
            course_code = int(re.findall(r'\d+', founded_schedule.text)[0])
            if course_code not in course_added:
                date = dates[0]
            else:
                date = dates[1]
            schedules_result.append(
                Schedule(
                    course_code=course_code,
                    date=date,
                    page_link=link_rasp
                )
            )
        print("Parsing schedule page done!")
        return schedules_result

    @staticmethod
    def _download_file(id):
        temp_formats = []
        # Если pdf-файл залит в cloud.mail.ru
        if 'cloud.mail.ru' in id:
            try:
                part = id.rpartition('public/')[-1]  # Кусок будущей ссылки для скачивания
                name = id.rpartition('/')[-1]  # Будущее имя файла

                # Если файл уже скачан, то еще раз он качаться не будет
                if os.path.isfile(f'pdfs/{name}.pdf'):
                    return True

                # Парсим сайт cloud.mail.ru
                temp = requests.get(id)
                temp = temp.text

                # Магическим образом достаем ссылку для скачивания
                magic_link = Link.parse_raw(temp.partition('"weblink_get":')[2].partition(',"weblink')[0])
                pdf = requests.get(magic_link.url + f'/{part}')

                # Скачиваем нужный нам pdf-файл
                with open(f'pdfs/{name}.pdf', 'wb') as f:
                    f.write(pdf.content)
                return True

            # Отлов ошибок при скачивании, которые будут выводиться в консоль
            except Exception as ex:
                print(f'Не удалось скачать файл {id}, из-за {ex}')
                return False

        # Если pdf-файл залит на сайт колледжа
        else:
            name = id.rpartition('/')[-1]  # Будущее имя файла

            # Если файл уже скачан, то еще раз он качаться не будет
            if os.path.isfile(f'pdfs/{name}'):
                return True

            # Скачиваем нужный нам pdf-файл
            response = requests.get(id)
            temp_formats.append('pdf')
            with open(f'pdfs/{name}', 'wb') as f:
                f.write(response.content)
            return True

    def download_schedules(self, schedules: List[Schedule]):
        print("Загрузка расписаний...")
        for schedule in schedules:
            result_download = self._download_file(schedule.page_link)
            if not result_download:
                pass
        print("Загрузка расписаний завершена")


def main():
    while True:
        time.sleep(5)
        schedule_parser = ScheduleParser()
        schedules = schedule_parser.parse_schedule_page()
        schedule_parser.download_schedules(schedules=schedules)

