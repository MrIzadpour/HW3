class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullName(self):
        return f"{self.first_name} {self.last_name}"


class BankAccount:
    wage_amount = 600                       # کامزد برداشت یا انتقال ...
    minimum_balance = 10000                 # حداقل مانده حساب

    def __init__(self, owner: Customer, initial_balance: int = 0):
        self.__owner = owner
        self.__balance = initial_balance

    def __check_minimum_balance(self, amount_to_withdraw: int = 0):             # چک کردن حداقل حساب
        return (self.__balance - amount_to_withdraw) >= self.minimum_balance

    def set_owner(self, owner):             # تابع setter
        self.__owner = owner

    def get_owner(self):                    # تابع getter
        return self.__owner

    def withdraw(self, amount):             # برداشت از حساب
        assert self.__check_minimum_balance(amount + self.wage_amount), 'Minimum balance error'
        self.__balance -= amount            # برداشت میلغ مورد نظر
        self.__balance -= self.wage_amount  # برداشت کارمزد

    def deposit(self, amount):              # واریز وجه
        self.__balance += amount

    def get_balance(self):                  # مشاهده موجودی
        self.__balance -= self.wage_amount  # برداشت کارمزد
        return self.__balance

    def transfer(self, target_account, amount: int):
        self.withdraw(amount)               # برداشت از حساب خود
        target_account.deposit(amount)      # واریز به حساب مقصد

    @classmethod
    def change_wage(cls, new_amount):
        cls.wage_amount = max(new_amount, 0)                    # حداقل مقدار برابر صفر است

    @classmethod
    def change_min_balance(cls, new_amount):
        cls.minimum_balance = max(new_amount, 0)                # حداقل مقدار برابر صفر است


mohammad = Customer('mohammad', 'asghari')
samad = Customer('samad', 'ahmadvand')

mohammad_account = BankAccount(mohammad, 10000000)
samad_account = BankAccount(samad, 100000)

mohammad_account.deposit(25000)
print("mohammad account balance:", mohammad_account.get_balance())

mohammad_account.withdraw(10000)
print("mohammad account balance:", mohammad_account.get_balance())

mohammad_account.transfer(samad_account, 1000000)
