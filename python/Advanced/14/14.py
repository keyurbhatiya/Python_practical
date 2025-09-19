'''

Write a program in python to implement Salary printing file read operation. (File format: 
Employee No, name, deptno, basic, DA, HRA, Conveyance) should perform below 
operations. 
a) Print Salary Slip for given Employee Number 
b) Print Employee List for Given Department Number 


'''

# Function to read employee data from file
# Function to read employee data from file
def read_employee_data(file_name):
    employees = []
    try:
        with open(file_name, "r") as file:
            next(file)  # Skip the first line (header row)
            for line in file:
                data = line.strip().split(",")
                if len(data) == 7:  # Ensure correct format
                    emp_no, name, dept_no, basic, da, hra, conveyance = data
                    employees.append({
                        "emp_no": emp_no,
                        "name": name,
                        "dept_no": dept_no,
                        "basic": float(basic),  # Convert to float
                        "da": float(da),
                        "hra": float(hra),
                        "conveyance": float(conveyance)
                    })
    except FileNotFoundError:
        print("Error: Employee data file not found!")
    return employees


# Function to print salary slip for a given Employee Number
def print_salary_slip(employees, emp_no):
    for emp in employees:
        if emp["emp_no"] == emp_no:
            gross_salary = emp["basic"] + emp["da"] + emp["hra"] + emp["conveyance"]
            print(f"\nSalary Slip for Employee No: {emp_no}")
            print(f"Name: {emp['name']}")
            print(f"Department No: {emp['dept_no']}")
            print(f"Basic Salary: {emp['basic']}")
            print(f"DA: {emp['da']}")
            print(f"HRA: {emp['hra']}")
            print(f"Conveyance: {emp['conveyance']}")
            print(f"Gross Salary: {gross_salary}")
            return
    print(f"No employee found with Employee No: {emp_no}")

# Function to print Employee List for a given Department Number
def print_employee_list(employees, dept_no):
    found = False
    print(f"\nEmployee List for Department No: {dept_no}")
    for emp in employees:
        if emp["dept_no"] == dept_no:
            print(f"Employee No: {emp['emp_no']}, Name: {emp['name']}, Basic Salary: {emp['basic']}")
            found = True
    if not found:
        print("No employees found in this department.")

# Main function
def main():
    file_name = "advanced/employee_data.txt"  # Change this to your actual file path
    employees = read_employee_data(file_name)

    while True:
        print("\n1. Print Salary Slip for an Employee")
        print("2. Print Employee List for a Department")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_no = input("Enter Employee Number: ")
            print_salary_slip(employees, emp_no)
        elif choice == "2":
            dept_no = input("Enter Department Number: ")
            print_employee_list(employees, dept_no)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
