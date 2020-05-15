


from Application.DB.People import get_employees
from Application.Salary import calculate_salary
from datetime import datetime, date, time


def main():
    employees = get_employees()
    total_salary = calculate_salary(employees)
    print(f'Общая зарплата всех сотрудников составляет {total_salary} на дату {datetime.today().strftime("%d/%m/%Y")}')



if __name__ == '__main__':
    main()