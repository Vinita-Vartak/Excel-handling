from emp_classes import Employee, Address
import random

a1 = Address(area="Virat Nagar", pin=546374, city="Patna")
a2 = Address(area="Gomati", pin=572444, city="Pune")
a3 = Address(area="Anand Sagar", pin=576374, city="Thane")

adr_lst = [a1, a2, a3]


def get_name():
    name = ""
    for i in range(random.randint(4, 8)):
        single_char = chr(64 + random.randint(1, 26))
        name += single_char
    return name.title()


def get_emp_objs(no):
    emp_list = []
    for i in range(1, no+1):
        eid = 100 + i
        ename = get_name()
        esal = random.randint(50000, 98990)
        eadr = random.choice(adr_lst)
        emp_obj = Employee(eid=eid, ename=ename, esalary=esal, eadr=eadr)
        emp_list.append(emp_obj)
    return emp_list

all_emps = get_emp_objs(5)
# print(all_emps)
