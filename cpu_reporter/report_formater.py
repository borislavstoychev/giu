from datetime import datetime
from typing import List, Tuple
import matplotlib.pyplot as plt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import io
from email import encoders


def format_report(report: List[Tuple[datetime, int]]):
    return "\n".join([" Time: " + time.strftime("%H:%M:%S:%f") + " " + "CPU_workload: " + str(measurement) + "%" for
                      time, measurement in report])


def line_char(report):
    time = [time for time, _ in report]
    measurement = [measurement for _, measurement in report]
    f = plt.figure()
    plt.plot(time, measurement, color="red")
    plt.xlabel("Time")  # add X-axis label
    plt.ylabel("CPU Percentage Load")  # add Y-axis label
    plt.title("CPU report")
    binary = io.BytesIO()
    f.savefig(binary, bbox_inches="tight")# add title
    # plt.grid(True)
    # plt.close()

    email = MIMEMultipart()
    body = format_report(report)
    email.attach(MIMEText(body))
    part = MIMEBase("application", "octet-stream", Name="CPU reporter")
    binary.seek(0)
    part.set_payload(binary.read())
    encoders.encode_base64(part)
    email.attach(part)

    return email
