import pytest

from company import employees as date_employees
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


# def run_all_tests():

#     assert get_employee_by_id(employees, 1)["name"] == "Иван Петров"
#     assert get_salary_by_year(get_employee_by_id(employees, 1), 2025) == 4700
#     assert get_projects_by_year(get_employee_by_id(employees, 1), 2025) == 6
#     assert get_max_salary(get_employee_by_id(employees, 1)) == 5200
#     assert len(get_active_employees(employees)) > 0
#     assert len(get_fired_employees(employees)) == 4
#     assert get_average_salary(get_employee_by_id(employees, 1)) == 4525.0
#     assert get_total_salary(get_employee_by_id(employees, 1)) == 18100
#     assert get_total_projects(get_employee_by_id(employees, 1)) == 22

#     print("Все тесты успешно пройдены")


# if __name__ == "__main__":
#     run_all_tests()



@pytest.fixture
def employees():
    return date_employees


@pytest.fixture
def empty_list():
    return []

# get_employee_by_id

@pytest.mark.parametrize(
    "employee_id, expected_name",
    [(1, "Иван Петров"),
     (15, "Константин Зайцев")],
)


def test_get_employee_by_id_found(employees, employee_id, expected_name):
    emp = get_employee_by_id(employees, employee_id)
    assert emp is not None
    assert emp["name"] == expected_name


def test_get_employee_by_id_not_found(employees):
    assert get_employee_by_id(employees, 999) is None


def test_get_employee_by_id_empty_list(empty_list):
    assert get_employee_by_id(empty_list, 1) is None


# get_active_employees


def test_get_active_employees_count(employees):
    assert len(get_active_employees(employees)) == 11


def test_get_active_employees_only_active(employees):
    result = get_active_employees(employees)
    assert all(e["fire_year"] is None for e in result)


def test_get_active_employees_empty(empty_list):
    assert get_active_employees(empty_list) == []


# get_fired_employees

def test_get_fired_employees_count(employees):
    assert len(get_fired_employees(employees)) == 4


def test_get_fired_employees_empty(empty_list):
    assert get_fired_employees(empty_list) == []


# get_department_employees

def test_get_department_employees_finance(employees):
    id = {e["id"] for e in get_department_employees(employees, "Finance")}
    assert id == {3, 8, 15}


def test_get_department_employees_it(employees):
    id = {e["id"] for e in get_department_employees(employees, "IT")}
    assert id == {1, 5, 7, 11}


def test_get_department_employees_hr(employees):
    id = {e["id"] for e in get_department_employees(employees, "HR")}
    assert id == {2, 10}


def test_get_department_employees_empty(empty_list):
    assert get_department_employees(empty_list, "IT") == []


# get_hired_after

def test_get_hired_after_2018(employees):
    id = {e["id"] for e in get_hired_after(employees, 2018)}
    assert id == {1, 4, 6, 7, 9, 12, 14}


# get_older_than


def test_get_older_than_30(employees):
    ids = {e["id"] for e in get_older_than(employees, 30)}
    assert ids == {2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15}

# get_salary_by_year


def test_get_salary_by_year_first_year(employee_full_history):
    assert get_salary_by_year(employee_full_history, 2023) == 3900


def test_get_salary_by_year_last_year(employee_full_history):
    assert get_salary_by_year(employee_full_history, 2026) == 5200


#  get_projects_by_year 

def test_get_projects_by_year_last_year(employee_full_history):
    assert get_projects_by_year(employee_full_history, 2026) == 7


#  get_average_salary 

def test_get_average_salary_full_history(employee_full_history):
    # (3900 + 4300 + 4700 + 5200) / 4 = 4525.0
    assert get_average_salary(employee_full_history) == 4525.0


def test_get_average_salary_single_year(employee_single_year):
    # история из одного года → среднее = сама зарплата
    assert get_average_salary(employee_single_year) == 3500.0


#  get_max_salary 

def test_get_max_salary_full_history(employee_full_history):
    assert get_max_salary(employee_full_history) == 5200


def test_get_max_salary_single_year(employee_single_year):
    assert get_max_salary(employee_single_year) == 3500


#  get_total_salary 

def test_get_total_salary_full_history(employee_full_history):
    # 3900 + 4300 + 4700 + 5200 = 18100
    assert get_total_salary(employee_full_history) == 18100


def test_get_total_salary_single_year(employee_single_year):
    assert get_total_salary(employee_single_year) == 3500


#  get_total_projects 

def test_get_total_projects_full_history(employee_full_history):
    # 4 + 5 + 6 + 7 = 22
    assert get_total_projects(employee_full_history) == 22


def test_get_total_projects_single_year(employee_single_year):
    assert get_total_projects(employee_single_year) == 1

