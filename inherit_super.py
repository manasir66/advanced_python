#make classes, super classes and use inheritence

class Employee:

  def __init__(self, name, nic_no, salary):
    self.name = name
    self.nic_no = nic_no
    self.salary = salary


class Engineer(Employee):

  def __init__(self, name, nic_no, salary, engin_field):
    super().__init__(name, nic_no, salary)  #inheriting from the super class
    self.engin_field = engin_field


class Technician(Employee):

  def __init__(self, name, nic_no, salary, tech_zone):
    super().__init__(name, nic_no, salary)
    self.tech_zone = tech_zone


class Manager(Employee):

  def __init__(self, name, nic_no, salary, access_level):
    super().__init__(name, nic_no, salary)
    self.access_level = access_level