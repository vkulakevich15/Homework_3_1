# Поиск сотрудников
employees = [
    {
        "id": 1,
        "name": "Иван Петров",
        "department": "IT",
        "age": 28,
        "hire_year": 2021,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3900, "projects": 4},
            {"year": 2024, "salary": 4300, "projects": 5},
            {"year": 2025, "salary": 4700, "projects": 6},
            {"year": 2026, "salary": 5200, "projects": 7}
        ]
    },
    {
        "id": 2,
        "name": "Анна Сидорова",
        "department": "HR",
        "age": 35,
        "hire_year": 2018,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3200, "projects": 2},
            {"year": 2024, "salary": 3400, "projects": 3},
            {"year": 2025, "salary": 3600, "projects": 2},
            {"year": 2026, "salary": 3900, "projects": 1}
        ]
    },
    {
        "id": 3,
        "name": "Сергей Ковалев",
        "department": "Finance",
        "age": 41,
        "hire_year": 2016,
        "fire_year": 2025,
        "history": [
            {"year": 2023, "salary": 4100, "projects": 3},
            {"year": 2024, "salary": 4400, "projects": 4},
            {"year": 2025, "salary": 4700, "projects": 3}
        ]
    },
    {
        "id": 4,
        "name": "Мария Орлова",
        "department": "Marketing",
        "age": 30,
        "hire_year": 2020,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3500, "projects": 5},
            {"year": 2024, "salary": 3800, "projects": 4},
            {"year": 2025, "salary": 4100, "projects": 5},
            {"year": 2026, "salary": 4400, "projects": 6}
        ]
    },
    {
        "id": 5,
        "name": "Дмитрий Васильев",
        "department": "IT",
        "age": 38,
        "hire_year": 2017,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 4800, "projects": 6},
            {"year": 2024, "salary": 5200, "projects": 7},
            {"year": 2025, "salary": 5600, "projects": 8},
            {"year": 2026, "salary": 6100, "projects": 9}
        ]
    },
    {
        "id": 6,
        "name": "Ольга Мороз",
        "department": "Sales",
        "age": 27,
        "hire_year": 2023,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 2800, "projects": 2},
            {"year": 2024, "salary": 3200, "projects": 3},
            {"year": 2025, "salary": 3700, "projects": 4},
            {"year": 2026, "salary": 4300, "projects": 4}
        ]
    },
    {
        "id": 7,
        "name": "Алексей Романов",
        "department": "IT",
        "age": 33,
        "hire_year": 2019,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 4400, "projects": 5},
            {"year": 2024, "salary": 4700, "projects": 6},
            {"year": 2025, "salary": 5100, "projects": 7},
            {"year": 2026, "salary": 5500, "projects": 8}
        ]
    },
    {
        "id": 8,
        "name": "Елена Белова",
        "department": "Finance",
        "age": 46,
        "hire_year": 2015,
        "fire_year": 2024,
        "history": [
            {"year": 2023, "salary": 4300, "projects": 3},
            {"year": 2024, "salary": 4500, "projects": 2}
        ]
    },
    {
        "id": 9,
        "name": "Павел Никитин",
        "department": "Logistics",
        "age": 29,
        "hire_year": 2020,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3100, "projects": 4},
            {"year": 2024, "salary": 3400, "projects": 5},
            {"year": 2025, "salary": 3700, "projects": 5},
            {"year": 2026, "salary": 4000, "projects": 6}
        ]
    },
    {
        "id": 10,
        "name": "Наталья Фролова",
        "department": "HR",
        "age": 45,
        "hire_year": 2014,
        "fire_year": 2023,
        "history": [
            {"year": 2023, "salary": 3500, "projects": 1}
        ]
    },
    {
        "id": 11,
        "name": "Виктор Громов",
        "department": "IT",
        "age": 50,
        "hire_year": 2012,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 5800, "projects": 8},
            {"year": 2024, "salary": 6200, "projects": 8},
            {"year": 2025, "salary": 6500, "projects": 9},
            {"year": 2026, "salary": 6800, "projects": 10}
        ]
    },
    {
        "id": 12,
        "name": "Татьяна Волкова",
        "department": "Marketing",
        "age": 32,
        "hire_year": 2021,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3300, "projects": 3},
            {"year": 2024, "salary": 3600, "projects": 4},
            {"year": 2025, "salary": 3900, "projects": 4},
            {"year": 2026, "salary": 4200, "projects": 5}
        ]
    },
    {
        "id": 13,
        "name": "Андрей Егоров",
        "department": "Logistics",
        "age": 36,
        "hire_year": 2018,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3400, "projects": 4},
            {"year": 2024, "salary": 3600, "projects": 5},
            {"year": 2025, "salary": 3800, "projects": 6},
            {"year": 2026, "salary": 3900, "projects": 5}
        ]
    },
    {
        "id": 14,
        "name": "Юлия Краснова",
        "department": "Sales",
        "age": 31,
        "hire_year": 2019,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 3700, "projects": 5},
            {"year": 2024, "salary": 4000, "projects": 6},
            {"year": 2025, "salary": 4300, "projects": 6},
            {"year": 2026, "salary": 4600, "projects": 7}
        ]
    },
    {
        "id": 15,
        "name": "Константин Зайцев",
        "department": "Finance",
        "age": 44,
        "hire_year": 2013,
        "fire_year": 2025,
        "history": [
            {"year": 2023, "salary": 4500, "projects": 2},
            {"year": 2024, "salary": 4800, "projects": 3},
            {"year": 2025, "salary": 5100, "projects": 2}
        ]
    }
]

def get_employee_by_id(employees, employee_id):     # Вернуть сотрудника по ID
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None


def get_active_employees(employees):     # Вернуть список работающих сотрудников
    result = []
    for employee in employees:
        if employee["fire_year"] is None:
            result.append(employee)
    return result



def get_fired_employees(employees):    # Вернуть список уволенных сотрудников
    result = []
    for employee in employees:
        if employee["fire_year"] is not None:
            result.append(employee)
    return result

# def get_fired_employees(employees):
#     return list(filter(employees, lambda e: e["fire_year"] is not None))


def get_department_employees(employees, department):    # Вернуть список сотрудников указанного отдела
    return list(filter(lambda e: e["department"] == department, employees))


def get_hired_after(employees, year):    # Вернуть список сотрудников, принятых после указанного года
    return list(filter(lambda e: e["hire_year"] > year, employees))


def get_older_than(employees, age):    # Вернуть список сотрудников старше указанного возраста
    return list(filter(lambda e: e["age"] > age, employees))


# Работа с историей сотрудника

def get_salary_by_year(employee, year):     # Вернуть зарплату сотрудника за указанный год.Если год отсутствует, вернуть: None

    for item in employee["history"]:
        if item["year"] == year:
            return item["salary"]
    return None


def get_projects_by_year(employee, year):    # Вернуть количество проектов сотрудника за указанный год. Если год отсутствует, вернуть: None 
    
    for item in employee["history"]:
        if item["year"] == year:
            return item["projects"]
    return None


def get_average_salary(employee):     # Вернуть среднюю зарплату сотрудника за все годы
    if not employee["history"]:
        return None
    total = 0
    count = 0
    for item in employee["history"]:
        total += item["salary"]
        count += 1
    return total / count



def get_max_salary(employee):   # Вернуть максимальную зарплату сотрудника 
    best = None
    for item in employee["history"]:
        if best is None or item["salary"] > best:
            best = item["salary"]
    return best



def get_total_salary(employee):    # Вернуть суммарную зарплату сотрудника за все годы
    total = 0
    for item in employee["history"]:
        total += item["salary"]
    return total


def get_total_projects(employee):    # Вернуть суммарное количество проектов сотрудника за все годы
    total = 0
    for item in employee["history"]:
        total += item["projects"]
    return total


# def get_experience(employee, current_year):    # Вернуть стаж сотрудника.Если сотрудник работает/ Если сотрудник уволен



# Аналитика по компании
