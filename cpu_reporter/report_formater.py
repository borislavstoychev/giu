from datetime import datetime
from typing import List, Tuple


def format_report(report: List[Tuple[datetime, int]]):
    return "\n".join([time.strftime("%H:%M:%S") + " " + str(measurement) for time, measurement in report])
