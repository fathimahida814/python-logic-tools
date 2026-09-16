while True:
    print('--- Smart Expense Tracker ---')
    print('1. Add Expense')
    print('2. View All Expenses')
    print('3. View Summary')
    print('4.Search Expense')
    print('5.Exit')
    choice = input('Enter choice:')
    if choice == '5':
        break

    if choice == '1':
        date = input('Enter date :')
        category = input('Enter category: ')
        amount = input('Enter amount: ')
        file = open('expenses.csv', 'a')
        file.write(date + ',' +  category +
                    ',' + amount + '\n')
        file.close()
        print('Expense saved!')

    if choice == '2':
        file = open('expenses.csv', 'r')
        print('--- All Expenses ---')
        for line in file:
            print(line)
        file.close()

    if choice == '3':
        file = open('expenses.csv', 'r')
        total = 0
        for line in file:
            parts = line.split(',')
            amount = int(parts[2])
            total += amount
        file.close()
        print('Total expense:', total)

        if choice == '4':
            search = input('Enter category to search: ')
            file = open('expense.csv', 'r')
            found = False
            print('--- search results ---')
            for line in file:
                if search.lower() in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print('No expenses found for', search)
            file.close()