from PythonClasses.Account import Account

if __name__ == '__main__':
    account = Account("Sammy", 100.0)
    print("The initial information is:\n%s" % account.details())
    account.setName("Samuel")
    account.deposit(4000.0)
    print("The new information is:\n%s" % account.details())
    account.withdraw(750)
    print("The new information is:\n%s" % account.details())

