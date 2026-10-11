from utils import (
    employees,
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

def run_all_tests():

    assert get_employee_by_id(employees, 1)["name"] == "Иван Петров"
    assert get_salary_by_year(get_employee_by_id(employees, 1), 2025) == 4700
    assert get_projects_by_year(get_employee_by_id(employees, 1), 2025) == 6
    assert get_max_salary(get_employee_by_id(employees, 1)) == 5200
    assert len(get_active_employees(employees)) > 0
    assert len(get_fired_employees(employees)) == 4
    assert get_average_salary(get_employee_by_id(employees, 1)) == 4525.0
    assert get_total_salary(get_employee_by_id(employees, 1)) == 18100
    assert get_total_projects(get_employee_by_id(employees, 1)) == 22

    print("Все тесты успешно пройдены")


if __name__ == "__main__":
    run_all_tests()