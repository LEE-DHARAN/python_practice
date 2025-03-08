class PiggyBank:
    def __init__(self, money):
        self.__money = money 

    def check_money(self): 
        return f"You have ₹{self.__money} in your piggy bank!"

    def add_money(self, amount): 
        if amount > 0:
            self.__money += amount
            return f"₹{amount} added! Now you have ₹{self.__money}."
        else:
            return "You can't add negative money!"

# Creating Piggy Bank Object
my_piggy_bank = PiggyBank(100) 

# Checking Money (Using Getter)
print(my_piggy_bank.check_money())  

# Adding Money (Using Setter)
print(my_piggy_bank.add_money(50))  

