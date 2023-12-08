"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Contract:
    def __init__(self, contract_type, salary=None, hourly_rate=None):
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_rate = hourly_rate

class Commission:
    def __init__(self, commission_type, fixed_bonus=None, contracts_landed=None, commission_per_contract=None):
        self.commission_type = commission_type
        self.fixed_bonus = fixed_bonus
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

class Employee:
    def __init__(self, name, contract_type, salary=None, hourly_rate=None, hours_worked=None,
                 commission_type=None, fixed_bonus=None, contracts_landed=None, commission_per_contract=None):
        self.name = name
        self.contract = Contract(contract_type, salary, hourly_rate)
        self.hours_worked = hours_worked
        self.commission = Commission(commission_type, fixed_bonus, contracts_landed, commission_per_contract)

    def get_pay(self):
        total_pay = 0
        if self.contract.contract_type == "Salary":
            total_pay = self.contract.salary
        elif self.contract.contract_type == "Hourly":
            total_pay = self.contract.hourly_rate * self.hours_worked

        if self.commission.commission_type == "Fixed":
            total_pay += self.commission.fixed_bonus
        elif self.commission.commission_type == "Contract Landed":
            total_pay += self.commission.contracts_landed * self.commission.commission_per_contract

        return total_pay

    def __str__(self):
        pay_description = f"{self.name} works on a "
        if self.contract.contract_type == "Salary":
            pay_description += f"monthly salary of {self.contract.salary}"
        elif self.contract.contract_type == "Hourly":
            pay_description += f"contract of {self.hours_worked} hours at {self.contract.hourly_rate}/hour"

        if self.commission.commission_type == "Fixed":
            pay_description += f" and receives a bonus commission of {self.commission.fixed_bonus}"
        elif self.commission.commission_type == "Contract Landed":
            pay_description += f" and receives a commission for {self.commission.contracts_landed} contract(s) at {self.commission.commission_per_contract}/contract"

        total_pay = self.get_pay()
        pay_description += f". Their total pay is {total_pay}."

        return pay_description

# Employee instances as per the test file
billie = Employee(name='Billie', contract_type='Salary', salary=4000)
charlie = Employee(name='Charlie', contract_type='Hourly', hourly_rate=25, hours_worked=100)
renee = Employee(name='Renee', contract_type='Salary', salary=3000, commission_type='Contract Landed', contracts_landed=4, commission_per_contract=200)
jan = Employee(name='Jan', contract_type='Hourly', hourly_rate=25, hours_worked=150, commission_type='Contract Landed', contracts_landed=3, commission_per_contract=220)
robbie = Employee(name='Robbie', contract_type='Salary', salary=2000, commission_type='Fixed', fixed_bonus=1500)
ariel = Employee(name='Ariel', contract_type='Hourly', hourly_rate=30, hours_worked=120, commission_type='Fixed', fixed_bonus=600)
