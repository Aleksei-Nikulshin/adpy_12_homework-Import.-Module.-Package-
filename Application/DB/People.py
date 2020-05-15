
def get_employees():
    employees = {}
    while True:
        name = input('Введите фамилию сотрудника: ')
        salary = int(input('Введите зарплату сотрудника: '))
        employees.setdefault(name, salary)
        command = input('Введите цифру 1, если желаете продолжить ввод сотрудников или цифру 0, если желаете закончить ввод сотрудников: ')
        if command == str(0):
            break
    return employees