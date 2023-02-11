import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import athanRecordingList
import athanScrapers
import datetime
import eidDateRange
import eidRecordingList

athan_time_scraper = athanScrapers.MadridIslamicCenter()
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

eid_dates = {}
eid_dates.update(fitr_eid)
eid_dates.update(adha_eid)
