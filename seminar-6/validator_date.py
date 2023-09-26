# 2. В модуль с проверкой даты добавьте возможность запуска в
# терминале с передачей даты на проверку.


if __name__ == '__main__':
    from date import is_date_valid

    date = input("Введите дату в формате DD.MM.YYYY: ")
    if is_date_valid(date):
        print("Дата действительна.")
    else:
        print("Дата недействительна.")
