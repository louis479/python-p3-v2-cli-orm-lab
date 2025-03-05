from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for emp in employees:
        print(emp)


def find_employee_by_name():
    name = input("Enter the employee's name: ").strip()
    employee = Employee.find_by_name(name)
    
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")



def find_employee_by_id():
    emp_id = input("Enter the employee's id: ").strip()
    
    if emp_id.isdigit():
        employee = Employee.find_by_id(int(emp_id))
        if employee:
            print(employee)
        else:
            print(f"Employee {emp_id} not found")
    else:
        print("Invalid ID. Please enter a number.")



def create_employee():
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    department_id = input("Enter the employee's department id: ").strip()

    if not name or not job_title:
        print("Error creating employee: Name and job title must be non-empty strings.")
        return
    
    if not department_id.isdigit():
        print("Error creating employee: Department ID must be a number.")
        return

    try:
        employee = Employee.create(name, job_title, int(department_id))
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error creating employee: {e}")



def update_employee():
    emp_id = input("Enter the employee's id: ").strip()
    
    if not emp_id.isdigit():
        print("Invalid ID format. Please enter a number.")
        return
    
    employee = Employee.find_by_id(int(emp_id))
    
    if not employee:
        print(f"Employee {emp_id} not found")
        return

    new_name = input("Enter the employee's new name: ").strip()
    new_job_title = input("Enter the employee's new job title: ").strip()
    new_department_id = input("Enter the employee's new department id: ").strip()

    if not new_name or not new_job_title or not new_department_id.isdigit():
        print("Error: Invalid input. Name and job title must be non-empty, and department ID must be a number.")
        return

    try:
        employee.update(new_name, new_job_title, int(new_department_id))
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    emp_id = input("Enter the employee's id: ").strip()
    
    if not emp_id.isdigit():
        print("Invalid ID format. Please enter a number.")
        return
    
    employee = Employee.find_by_id(int(emp_id))
    
    if not employee:
        print(f"Employee {emp_id} not found")
        return

    employee.delete()
    print(f"Employee {emp_id} deleted")



def list_department_employees():
    dept_id = input("Enter the department's id: ").strip()
    
    if not dept_id.isdigit():
        print("Invalid department ID. Please enter a number.")
        return
    
    department = Department.find_by_id(int(dept_id))
    
    if not department:
        print(f"Department {dept_id} not found")
        return

    employees = department.employees()
    if employees:
        for emp in employees:
            print(emp)
    else:
        print(f"No employees found in Department {dept_id}")
