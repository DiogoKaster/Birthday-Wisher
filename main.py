import smtplib
import random as r
import pandas as pd
import datetime as dt

PLACEHOLDER = "[NAME]"
LOGIN = "your email"
PASSWORD = "your password"

data = pd.read_csv("birthdays.csv").to_dict(orient="records")

now = dt.datetime.now()
today_day = now.day
today_month = now.month
for lista in data:
    if (today_day == lista['day']) and (today_month == lista['month']):

        with open(f"./letter_templates/letter{r.randint(1, 4)}.txt") as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace(PLACEHOLDER, lista['name'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=LOGIN, password=PASSWORD)
            connection.sendmail(
                from_addr=LOGIN,
                to_addrs=lista['email'],
                msg=f"Subject:Parabens amigo\n\n{new_letter}"
            )
