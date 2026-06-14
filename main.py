##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day
df = pandas.read_csv("birthdays.csv")
for i,r in df.iterrows():
    if r["month"] == month and r["day"] == day:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        with open(f"letter_templates/letter_{random.randint(1, 4)}.txt", 'r') as letter:
            bday_letter = letter.read()
            bday_letter = bday_letter.replace("[NAME]", r["name"])

# 4. Send the letter generated in step 3 to that person's email address.

        my_email = "goolor.love.isthebest@gmail.com"
        my_password = "xpup otrj smmu ujtx"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=r["email"],
                                msg="Subject: Happy Birthday\n"
                            f"From: {my_email}\n"
                            f"To: {r["email"]}\n"
                            "\n"
                            f"{bday_letter}")
