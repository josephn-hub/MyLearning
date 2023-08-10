from dataclasses import dataclass
import logging
from datetime import datetime, date
from enum import Enum

import pydantic
from pydantic import BaseModel


logging.basicConfig(filename="dataclass.log", level=logging.INFO, format='%(asctime)s - %(message)s')

@dataclass
class Employee():
    name: str
    designation: str
    salary: int



employee = Employee(name='Joseph', designation='Archotectl', salary=300)
logging.warning(print(employee.salary))

fruits = ['mango', 'appl', 'grapes', 'strawberry']

quantity = [50, 50, 70, 80]

for index, mapping in enumerate(zip(fruits, quantity)):
    print(index, mapping)


date_time = "2023-05-25 20:10:50"

strp_time_change = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
print(strp_time_change)

current_time = datetime.now()
strf_time_change = current_time.strftime("%Y/%m/%d %H:%M:%S")
print(strf_time_change)


class Family(Enum):
    FIRST_FAMILY = "KAMBHAM"
    SECOND_FAMILY = "MAMIDIAPLLI"


family = Family(ka)
print(family.FIRST_FAMILY)