from datetime import date
import inflect
import sys

def main():
    birthdate = input("Date of Birth: ")

    try:
        year, month, day = birthdate.split("-")
        birthday = date(int(day), int(month), int(year))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    days = (today - birthday).days
    minutes = days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes)

    print(words.capitalize() + " minutes")

if __name__ == "__main__":
    main()
