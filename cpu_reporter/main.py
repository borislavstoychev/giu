from datetime import timedelta
from mail_sender import send_mail
from report_formater import format_report
from report_generator import generate_report


def main():
    report = generate_report(duration=timedelta(seconds=2))
    formatted = format_report(report)
    send_mail(formatted)

if __name__ == "__main__":
    main()