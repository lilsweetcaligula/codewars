def find_employees_role(name):
    for employee in employees:
        employee_name = ' '.join((employee['first_name'], employee['last_name']))
        if name == employee_name:
            return employee['role']
    return 'Does not work here!'