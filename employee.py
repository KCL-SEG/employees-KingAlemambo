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


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
