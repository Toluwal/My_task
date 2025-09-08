# class NaijaPhone:
#     def __init__(self, brand, model, network_provider):
#         self.brand = brand
#         self.model = model
#         self.network_provider = network_provider
#         self.airtime_balance = 0
#         self.data_balance = 0
#         self.is_on = False
    
#     def power_on(self):
#         self.is_on = True
#         return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
#     def buy_airtime(self, amount):
#         self.airtime_balance += amount
#         return f" ₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
#     def make_call(self,message, number):
#         if self.is_on and self.airtime_balance > 0:
#             self.airtime_balance -= 10
#             return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
#         return "Cannot make call. Check your phone power and airtime balance"
    
#     def send_sms(self, message, number):
#             if self.airtime_balance >= 4:
#                 self.airtime_balance -= 4
#                 return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
#             return "Insufficient airtime to send SMS"


# print(NaijaPhone.buy_airtime(500))
# #print(f"Bank: {adunni_account.bank_name}")
# print(f"NaijaPhone: {brand.buyairtime}")


class NigerianBankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance   # Protected attribute
        self.pin = "1234"   # Private attribute
        self._transaction_history = []     # Protected attribute

    # Public methods - anyone can use these
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited ₦{amount:,}")
            return f"₦{amount:,} deposited successfully"
        return "Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):   # Uses private method
            if amount <= self.balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew ₦{amount:,}")
                return f"₦{amount:,} withdrawn successfully"
            return "Insufficient funds"
        return "Invalid pin"
    
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Current balance: ₦{self._balance:,}"
        return "Invalid PIN"
    
    # Private method - only the class can use this

    def __verify_pin(self, entered_pin):
        return (entered_pin == self.__pin)
    
    # Protected method - subclasses can use this
    def _get_transaction_history(self):
        return self._transaction_history.copy()

# Using the encapsulated account
# ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# # These work - public interface
# print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
# print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
# print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000

