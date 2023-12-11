from datetime import date, datetime


def get_birthdays_per_week(users):
    result = {}

    DAYS_OF_WEEK = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

    if not users:
        return result

    this_date = date.today()
    #this_date = date(year=2023, month=12, day=27)
    this_year = this_date.year

    for user in users:
        user_birthday_in_this_year = user["birthday"].replace(year = this_year)
        user_birthday_in_next_year = user["birthday"].replace(year = this_year + 1)
        
        delta_1 = user_birthday_in_this_year - this_date
        delta_2 = user_birthday_in_next_year - this_date        

        if int(delta_1.days) >= 0 and int(delta_1.days) < 7:
            # ДР в цьому році на протязі тижня
            user_closest_birthday = user_birthday_in_this_year
        elif int(delta_1.days) < 0 and int(delta_2.days) < 7:            
            # ДР в наступному році на протязі тижня
            user_closest_birthday = user_birthday_in_next_year            
        else:
            continue

        user_closest_birthday_day = user_closest_birthday.weekday()

        if user_closest_birthday_day == 5 or user_closest_birthday_day == 6:
            user_closest_birthday_day = 0

        result.setdefault(DAYS_OF_WEEK[user_closest_birthday_day], []).append(user["name"])
    
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Oleh Davyd", "birthday": datetime(1955, 1, 3).date()},
        {"name": "Oleh Davyd11", "birthday": datetime(1984, 12, 30).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
