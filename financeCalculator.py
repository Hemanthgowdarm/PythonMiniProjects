def calculateFinances(monthlyIncome: float, taxRate: float, expenses: list, currency: str) -> None:
    # Doing some math to calculate finanses
    monthlyIncome = monthlyIncome - sum(expenses)
    monthlyTax: float = monthlyIncome * (taxRate / 100)
    monthlyNetIncome: float = monthlyIncome - monthlyTax
    yearlyIncome: float = monthlyIncome * 12
    yearlyTax: float = monthlyTax * 12
    yearlyNetIncome: float = yearlyIncome - yearlyTax 

    # Printing the calculated values in nice way
    print("-------------------------------")
    print(f"Monthly Income: {currency}{monthlyIncome:,.2f}")
    print(f"Tax Rate: {taxRate:,.0f}%")
    print(f"Monthly Tax: {currency}{monthlyTax:,.2f}")
    print(f"Monthly Net Income: {currency}{monthlyNetIncome:,.2f}")
    print(f"Yearly Salary: {currency}{yearlyIncome:,.2f}")
    print(f"Yearly Tax Paid: {currency}{yearlyTax:,.2f}")
    print(f"Yearly Net Income: {currency}{yearlyNetIncome:,.2f}")
    print("-------------------------------")


def main() -> None:
    # Getting some inputs to calculate finanses with exception handling for ValueError and value out of range 
    while(True):
        try:
            monthlyIncome: float = float(input("Enter Your Monthly Income: "))
            break
        except ValueError:
            print("Incorrect Input!")
            continue
    while(True):
        try:
            taxRate: float = float(input("Enter Tax Rate: "))            
            if 0 <= taxRate <= 100:
                break
            else:
                print("Value must be between 0 and 100")
        except ValueError:
            print("Incorrect Input!")
            continue
    while(True):
        try:
            noOfExpenses: int = int(input("Enter Number of Eaxpenses: "))            
            break
        except ValueError:
            print("Incorrect Input!")
            continue
    
    expenses: list = []

    for i in range(noOfExpenses):
        while(True):
            try:
                expense: float = float(input(f"Enter Expense {i+1} : "))            
                break
            except ValueError:
                print("Incorrect Input!")
                continue
        
        expenses.append(expense)
    
    # Calling method to calculate finanses of a person
    calculateFinances(monthlyIncome, taxRate, expenses, "Rs")

if __name__ == "__main__":
    main()