class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def onboarding(self):
        self._attend_orientation()
        self._fill_out_paperwork()
        self._add_to_payroll()

    def _attend_orientation(self):
        ...

    def _fill_out_paperwork(self):
        ...

    def _add_to_payroll(self):
        ...
