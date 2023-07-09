class CommonMethod:
    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)


class Employee(CommonMethod):
    def __init__(self, eid, ename, esalary, eadr):
        self.EmpID = eid
        self.EmpName = ename
        self.EmpSalary = esalary
        self.EmpAddress = eadr


class Address(CommonMethod):
    def __init__(self, area, pin, city):
        self.Area = area
        self.Pincode = pin
        self.City = city


if __name__ == '__main__':
    adre_obj = Address("Baner", 463478, "Pune")
    emp_obj = Employee(101, "vinita", 87790, adre_obj)
    print(emp_obj)
