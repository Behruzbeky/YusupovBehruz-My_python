from datetime import datetime, date

def age_calculator():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - date(today.year, today.month-1, 1)).days
    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")

age_calculator()





from datetime import datetime, date

def days_until_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today
    print(f"Days until your next birthday: {delta.days}")

days_until_birthday()





from datetime import datetime, timedelta

def meeting_scheduler():
    now_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))

    start = datetime.strptime(now_str, "%Y-%m-%d %H:%M")
    end = start + timedelta(hours=duration_hours, minutes=duration_minutes)

    print(f"The meeting will end at: {end.strftime('%Y-%m-%d %H:%M')}")

meeting_scheduler()





from datetime import datetime
import pytz

def timezone_converter():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_zone = input("Enter your current timezone (e.g., Asia/Tashkent): ")
    to_zone = input("Enter target timezone (e.g., Europe/London): ")

    naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    local_dt = pytz.timezone(from_zone).localize(naive_dt)
    target_dt = local_dt.astimezone(pytz.timezone(to_zone))

    print(f"Time in {to_zone}: {target_dt.strftime('%Y-%m-%d %H:%M')}")

timezone_converter()




from datetime import datetime
import time

def countdown_timer():
    future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        if future <= now:
            print("⏰ Time's up!")
            break
        remaining = future - now
        print(f"Time left: {remaining}", end="\r")
        time.sleep(1)

countdown_timer()






import re

def email_validator():
    email = input("Enter an email address: ")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        print("Valid email ✅")
    else:
        print("Invalid email ❌")

email_validator()




def phone_formatter():
    number = input("Enter a 10-digit phone number: ")
    if len(number) == 10 and number.isdigit():
        formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
        print("Formatted:", formatted)
    else:
        print("Invalid phone number!")

phone_formatter()




import re

def password_checker():
    password = input("Enter a password: ")
    strength = []

    if len(password) >= 8:
        strength.append("✓ Length is good")
    else:
        strength.append("✗ Too short (min 8 characters)")

    if re.search(r"[A-Z]", password):
        strength.append("✓ Has uppercase")
    else:
        strength.append("✗ Missing uppercase")

    if re.search(r"[a-z]", password):
        strength.append("✓ Has lowercase")
    else:
        strength.append("✗ Missing lowercase")

    if re.search(r"\d", password):
        strength.append("✓ Has digit")
    else:
        strength.append("✗ Missing digit")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength.append("✓ Has special character")
    else:
        strength.append("✗ Missing special character")

    print("\nPassword Strength Check:")
    for line in strength:
        print(line)

password_checker()





def word_finder():
    text = """Python is powerful. Python is easy to learn. Python is everywhere."""
    word = input("Enter a word to search for: ")
    occurrences = [i for i, w in enumerate(text.split()) if word.lower() == w.lower().strip(".,!")]
    if occurrences:
        print(f"Found '{word}' at positions: {occurrences}")
    else:
        print(f"'{word}' not found.")

word_finder()





import re

def date_extractor():
    text = input("Enter a text with dates: ")
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"  # YYYY-MM-DD format
    matches = re.findall(pattern, text)
    if matches:
        print("Dates found:", matches)
    else:
        print("No dates found.")

date_extractor()


