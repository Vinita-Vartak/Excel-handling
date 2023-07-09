from emp_abstraction import EmpAbstraction
from emp_classes import Employee, Address
from emp_excel import FILE_PATH, load_excel_file, FILE_PATH_2
from emp_data import get_emp_objs
import csv


class EmpOperation(EmpAbstraction):
    def write_headers(self):
        workbook, sheet = load_excel_file()
        MAIN_HEADERS = "ID Name Salary Address".split()
        for i in range(1, 5):
            sheet.cell(row=1, column=i).value = MAIN_HEADERS[i-1]
        sheet.merge_cells("D1:F1")
        ADR_HEADERS = "Area Pincode City".split()
        for j in range(4, 7):
            sheet.cell(row=2, column=j).value = ADR_HEADERS[j-4]
        workbook.save(FILE_PATH)

    def write_data(self, number):
        workbook, sheet = load_excel_file()
        all_emps = get_emp_objs(number)
        counter = sheet.max_row + 1
        for emp in all_emps:
            sheet.cell(row=counter, column=1).value = 100 + sheet.max_row - 1
            sheet.cell(row=counter, column=2).value = emp.EmpName
            sheet.cell(row=counter, column=3).value = emp.EmpSalary
            sheet.cell(row=counter, column=4).value = emp.EmpAddress.Area
            sheet.cell(row=counter, column=5).value = emp.EmpAddress.Pincode
            sheet.cell(row=counter, column=6).value = emp.EmpAddress.City
            counter += 1
        workbook.save(FILE_PATH)

    def read_data(self):
        workbook, sheet = load_excel_file()
        for i in range(3, sheet.max_row + 1):
            id = sheet.cell(row=i, column=1).value
            name = sheet.cell(row=i, column=2).value
            salary = sheet.cell(row=i, column=3).value
            area_1 = sheet.cell(row=i, column=4).value
            pincode = sheet.cell(row=i, column=5).value
            city = sheet.cell(row=i, column=6).value
            adre_obj = Address(area_1, pincode, city)
            emp_obj = Employee(id, name, salary, adre_obj)
            print(emp_obj)
            
    def excel_to_csv(self):
        workbook, sheet = load_excel_file()
        with open(FILE_PATH_2, 'w',newline='') as file:
            writer = csv.writer(file)           
            for row in sheet.iter_rows(values_only=True):
                writer.writerow(row)
        


if __name__ == "__main__":

    obj = EmpOperation()

    print(f'''
    Welcome to Data
    Press option for
    H--- Headers
    W--- Write
    R--- Read
    C--- CSV
    E--- Exit
          ''')
    user_inp = input("Enter Your choice:-").upper()
    if user_inp == 'E':
        print("Thank you.")
    elif user_inp == 'H':
        obj.write_headers()
    elif user_inp == 'W':
        data_insert = int(input("enter the number:- "))
        obj.write_data(data_insert)
    elif user_inp == 'R':
        obj.read_data()
    elif user_inp == 'C':
        obj.excel_to_csv()
    else:
        print("Enter valid")

    # obj.write_headers()
    # obj.write_data()
    # obj.read_data()
