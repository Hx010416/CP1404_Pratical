"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
def get_income_input(month):
    return float(input(f"Enter income for month {month}: "))


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = get_income_input(month)
        incomes.append(income)
    print_report(incomes)


if __name__ == '__main__':
    main()
