revenue = int(input('Enter revenue of your company: '))
expenses = int(input('Enter expenses of your company: '))
if revenue > expenses:
    humans = int(input('Enter the number of employees '))
    revenue_1 = int((revenue / expenses) * 100)
    profit_per_emp = int(revenue / humans)
    print(f'You make a profit, profitability - {revenue_1}%')
    print(f'The profit per person is {profit_per_emp}')

if revenue < expenses:
    print('You work at a loss')
