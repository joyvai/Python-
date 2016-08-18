class BankAccount:

	def __init__(self):
		self.balance = 0
	def withdraw(self,amount):
		self.balance -= amount
		return self.balance
	def deposit(self,amount):
		self.balance += amount
		return self.balance

a = BankAccount()
b = BankAccount()

print a.deposit(100) # BankAccount.deposit
print b.deposit(50)
print a.withdraw(10) # 90
print b.withdraw(10) # 40
