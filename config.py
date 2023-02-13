import datetime

import athanRecordingList
import athanScrapers
import eidDateRange
import eidRecordingList

athan_time_scraper = athanScrapers.MadridIslamicCenter()
athan_recordings = [
    athanRecordingList.Sanaa,
    athanRecordingList.DubaiMall,
    athanRecordingList.Abdulbasit,
    athanRecordingList.AhmedAlhadad,
    athanRecordingList.Algeria,
    athanRecordingList.HasanSalah,
    athanRecordingList.Mecca,
    athanRecordingList.MohammedSalahaldin,
    athanRecordingList.Quds,
]

eid_recordings = [
    eidRecordingList.EidTakbir
]

fitr_eid = datetime.datetime(2023, 4, 22)
adha_eid = datetime.datetime(2023, 6, 29)

eid_dates = {}
eid_dates.update(eidDateRange.FitrEid(date=fitr_eid).takbeer_date_athan_range)
eid_dates.update(eidDateRange.AdhaEid(date=adha_eid).takbeer_date_athan_range)
