import datetime
import random
import time
from typing import List, Dict

import pause
from prettytable import PrettyTable

import athanRecordingList
import athanScrapers
import eidDateRange
import eidRecordingList
from athanScrapers import AthanScraper
from recording import Recording


def main(athan_scraper: AthanScraper, athan_recordings_list: List[Recording],
         eid_recordings_list: List[Recording], eid_date_range: Dict[datetime.date, List[bool]]) -> None:
    while True:
        time_now = datetime.datetime.now()
        athan_time = athan_scraper.get_athan_times(time_now)

        eid_period = time_now.date() in eid_date_range

        R = "\033[0;31;40m"  # RED
        G = "\033[0;32;40m"  # GREEN
        Y = "\033[0;33;40m"  # Yellow
        B = "\033[0;34;40m"  # Blue
        N = "\033[0m"  # Reset

        color = random.choice([R, G, Y, B])

        table = PrettyTable()
        table.title = color + f"({time_now.strftime('%A')}) {time_now.date()}" + N
        table.field_names = ["Athan", "Time"]
        table.add_rows(
            list(
                zip(
                    list(athan_time.index.values),
                    list(
                        athan_time.apply(
                            lambda t: datetime.datetime.strftime(t, "%H:%M")
                        )
                    ),
                )
            )
        )
        print(table)

        tmp_athan_time = athan_time[athan_time >= time_now]

        while tmp_athan_time.size:
            next_athan = tmp_athan_time[0]
            pause.until(next_athan)

            athan_sound: Recording = random.choice(athan_recordings_list)
            athan_sound.play_recording()

            if eid_period:
                # TODO: Test
                takbeer_times = eid_date_range.get(time_now.date())
                current_athan_index = athan_time.index.get_loc(next_athan.index)

                if takbeer_times[current_athan_index]:
                    time.sleep(5)
                    eid_sound: Recording = random.choice(eid_recordings_list)
                    eid_sound.play_recording()

            tmp_athan_time = tmp_athan_time[1:]

        tomorrow = time_now.date() + datetime.timedelta(days=1)
        tomorrow = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 1, 0)
        print(f"Pausing until {tomorrow}", end="\r")
        pause.until(tomorrow)


if __name__ == '__main__':
    madrid_islamic_center = athanScrapers.MadridIslamicCenter()
    athan_recordings = [
        athanRecordingList.Sanaa(),
        athanRecordingList.DubaiMall(),
        athanRecordingList.Abdulbasit(),
        athanRecordingList.AhmedAlhadad(),
        athanRecordingList.Algeria(),
        athanRecordingList.HasanSalah(),
        athanRecordingList.Mecca(),
        athanRecordingList.MohammedSalahaldin(),
        athanRecordingList.Quds(),
    ]

    eid_recordings = [
        eidRecordingList.EidTakbir()
    ]

    fitr_eid = eidDateRange.FitrEid(date=datetime.datetime(2023, 4, 22)).takbeer_date_athan_range
    adha_eid = eidDateRange.AdhaEid(date=datetime.datetime(2023, 6, 29)).takbeer_date_athan_range

    main(athan_scraper=madrid_islamic_center, athan_recordings_list=athan_recordings,
         eid_recordings_list=eid_recordings, eid_date_range=fitr_eid | adha_eid)
