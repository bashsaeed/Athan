import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class EidDateRange(ABC):
    date: datetime.datetime
    takbeer_date_athan_range: Dict[datetime.date, List[bool]] = field(init=False, default_factory=dict)

    @abstractmethod
    def calculate_date_range(self) -> None:
        """
        {datetime.date: [1,0,0,0,0]} -> only after fajr
        {datetime.date: [0,0,0,0,1]} -> only after ishaa
        {datetime.date: [1,1,1,1,1]} -> after every athan
        """
        pass

    def __post_init__(self) -> None:
        self.calculate_date_range()


class FitrEid(EidDateRange):
    def calculate_date_range(self) -> None:
        # after isha, the night before eid
        self.takbeer_date_athan_range.update(
            {self.date.date() - datetime.timedelta(days=1): [False, False, False, False, True]})

        # after fajr, on the day of eid
        self.takbeer_date_athan_range.update({self.date.date(): [True, False, False, False, False]})


class AdhaEid(EidDateRange):
    def calculate_date_range(self) -> None:
        # 3 days after eid
        [
            self.takbeer_date_athan_range.update(
                {self.date.date() + datetime.timedelta(days=x): [True, True, True, True, True]})
            for x in range(1, 4)
        ]

        # on the day of eid
        self.takbeer_date_athan_range.update({self.date.date(): [True, True, True, True, True]})

        # 9 days before eid
        [
            self.takbeer_date_athan_range.update(
                {self.date.date() - datetime.timedelta(days=x): [True, True, True, True, True]})
            for x in range(1, 10)
        ]

