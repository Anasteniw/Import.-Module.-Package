from application import salary
from application.db import people
import datetime



if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    
date_today = datetime.date.today()
print(date_today)
