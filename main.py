# WARNING: THIS REQUIRES EMAIL AND PASSWORD AS PLAINTEXT. FOR LOCAL USE ONLY.
# USE COMMERCIALLY AT YOUR OWN RISK

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "" # insert your email here
MY_PASSWORD = "" # insert your password here

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_{random.randint(1, 5)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection: #see below for other email servers
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
  # smtp.gmail.com for gmail
#   smtp-mail.outlook.com for hotmail/outlook
  # smtp.mail.yahoo.com for yahoo
#   smtp.rediffmailpro.com for rediffmail
  # smtp.vsnl.net for VSNL (idk who uses that nowadays)
   
#   Port number 465 for SSl [outdated]
  # Port number 587 for TLS [used for security - see connection.starttls() at line 24]
   
# Made with ❤️🍵 by @davidvaz1 on GitHub
