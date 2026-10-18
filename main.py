from company import employees
from utils import (
    get_employee_by_id,
    get_active_employees,
    get_fired_employees,
    get_department_employees,
    get_hired_after,
    get_older_than,
    get_salary_by_year,
    get_projects_by_year,
    get_average_salary,
    get_max_salary,
    get_total_salary,
    get_total_projects,
)

def show_menu():
    print("\n=== Анализ сотрудников ===")
    print("1. Все сотрудники")
    print("2. Сотрудник по ID")
    print("3. Работающие сотрудники")
    print("4. Уволенные сотрудники")
    print("5. Сотрудники отдела")
    print("6. Принятые после года")
    print("7. Старше возраста")
    print("8. Зарплата сотрудника за год")
    print("9. Проекты сотрудника за год")
    print("10. Средняя зарплата сотрудника")
    print("11. Максимальная зарплата сотрудника")
    print("12. Суммарная зарплата сотрудника")
    print("13. Суммарные проекты сотрудника")
    print("0. Выход")
