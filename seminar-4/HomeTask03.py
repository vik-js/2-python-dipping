# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
# операции — функции. Дополнительно сохраняйте все операции поступления
# и снятия средств в список.

account_status = 0
CHARGE = 1.5 / 100
MIN_LIM_OUT = 30
MAX_LIM_OUT = 600
BONUS = 3
TAX = 10


bankomat_action = int(input('Выберите действие (1 - Пополнить, 2 - Снять, 3 - выйти): '))


def cash_in(account_stat):
    global account_status
    print(f'На вашем счету: {account_status} у.е.')
    cash_in_action = int(input('Введите сумму пополнения: '))
    if cash_in_action % 50 == 0:
         account_status = int(account_status) + cash_in_action
         print(f'Сумма успешно внесена, на вашем счету: {account_status} у.е.')
    else:
        print('Внести можно только купюры кратные 50-ти!')


def cash_out(account_stat):
    global account_status
    print(f'На вашем счету: {account_status} у.е.')
    cash_out_action = int(input('Введите сумму снятия: '))
    if cash_out_action % 50 == 0:
        if cash_out_action < account_status:
            account_status = account_status - cash_out_action - (cash_out_action * CHARGE)
            print(f'Сумма успешно снята, на вашем счету: {account_status} у.е.')
        else:
            print('На счету недостаточно средств!')
    else:
        print('Снять можно только купюры кратные 50-ти!')


if bankomat_action == 1:
    cash_in(account_status)
elif bankomat_action == 2:
    cash_out(account_status)
elif bankomat_action == 3:
    print("До встречи! =)")
    exit
else:
    print("Введено недопустимое значение!")
