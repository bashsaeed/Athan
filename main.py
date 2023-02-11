import datetime
import random
from typing import List

import pause
from prettytable import PrettyTable

import athanRecordingList
import athanScrapers
from athanRecording import AthanRecording
from athanScrapers import AthanScraper


def main(athan_scraper: AthanScraper, athan_recordings_list: List[AthanRecording]) -> None:
    while True:
        time_now = datetime.datetime.now()
        athan_time = athan_scraper.get_athan_times(time_now)

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

        athan_time = athan_time[athan_time >= time_now]

        while athan_time.size:
            next_athan = athan_time[0]
            pause.until(next_athan)

            athan_sound: AthanRecording = random.choice(athan_recordings_list)
            athan_sound.play_athan()

            athan_time = athan_time[1:]

        tomorrow = time_now.date() + datetime.timedelta(days=1)
        tomorrow = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 1, 0)
        print(f"Pausing until {tomorrow}", end="\r")
        pause.until(tomorrow)


if __name__ == '__main__':
    madrid_islamic_center = athanScrapers.MadridIslamicCenter()
    athan_recordings = [
        athanRecordingList.SanaaAthan(),
        athanRecordingList.DubaiMallAthan(),
        athanRecordingList.AbdulbasitAthan(),
        athanRecordingList.AhmedAlhadadAthan(),
        athanRecordingList.AlgeriaAthan(),
        # EidTakbir(),
        athanRecordingList.HasanSalahAthan(),
        athanRecordingList.MeccaAthan(),
        athanRecordingList.MohammedSalahaldinAthan(),
        athanRecordingList.QudsAthan(),
    ]
    main(athan_scraper=madrid_islamic_center, athan_recordings_list=athan_recordings)
