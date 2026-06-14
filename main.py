import datetime as dt
import smtplib
import random
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with open("quotes.txt", "r") as quotes:
        quotes_str = quotes.read()
        quotes_list = quotes_str.splitlines()
    quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="24AyaanDube@lgs.slough.sch.uk",
                            msg = "Subject: Good morning\n"
                            f"From: {MY_EMAIL}\n"
                            "To: 24AyaanDube@lgs.slough.sch.uk\n"
                            "\n"
                            "Hello,\n"
                            "I know this is probably the day you hate the most so here's some motivation:\n"
                            f"{quote}")
        print("email sent")
