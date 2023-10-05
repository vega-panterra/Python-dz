# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

START_BALANCE = 0
DEPOSIT = 50
WITHDRAW_FACTOR = 50
COMISSION = 0.015
MIN_LIMIT = 30
LIMIT_MAX = 600
THE_THIRD_OPERATION = 3
INTEREST_PERCENT = 0.003
MAX_LIMIT = 5_000_000
WEALTH_TAX = 0.010

balance = START_BALANCE
count = 0
operation = []


def deposit_account(acc_balance, operation_count, operation_list):
    deposit_amount = int(input(f'Введите сумму пополнения, кратную {DEPOSIT}: '))
    if deposit_amount > 0 and deposit_amount % DEPOSIT == 0:
        acc_balance += deposit_amount
        operation_list.append(deposit_amount)
    else:
        print(f'Сумма пополнения не кратна {DEPOSIT}')

    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1

    return acc_balance, operation_count, operation_list


def withdraw_account(acc_balance, operation_count, operation_list):
    withdraw_amount = int(input(f'Введите сумму снятия, кратную {WITHDRAW_FACTOR}.\n'
                                f'Нельзя снять больше, чем на счете: '))

    if withdraw_amount % WITHDRAW_FACTOR == 0:
        percent = balance * COMISSION
        if percent < MIN_LIMIT:
            percent = MIN_LIMIT
        elif percent > LIMIT_MAX:
            percent = LIMIT_MAX

        if withdraw_amount + percent > acc_balance:
            print('Недостаточно средств на счете')
        else:
            acc_balance -= withdraw_amount + percent
            operation_list.append(int(-withdraw_amount - percent))
    else:
        print(f'Сумма снятия не кратна {WITHDRAW_FACTOR}')
    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


while True:

    if balance > MAX_LIMIT:
        tax = balance * WEALTH_TAX
        balance -= tax
        print(f'Баланс вашего счета после удержания налога на богатство: {balance:.0f}')
        operation.append(int(-tax))
    if count % THE_THIRD_OPERATION == 0:
        interest = balance * INTEREST_PERCENT
        balance += interest
        print(f'Баланс вашего счета после начисления процентов: {balance:.0f}')
        operation.append(int(interest))
    operation = input(f'Для работы с банкоматом выберите действие:\n1 - пополнить\n'
                      f'2 - снять\n3 - выйти\n')
    match operation:
        case '1':
            balance, count, operation = deposit_account(balance, count, operation)
        case '2':
            balance, count, operation = withdraw_account(balance, count, operation)
        case '3':
            print(f'Баланс вашего счета: {balance:.0f}')
            break
        case _:
            break

print(operation)