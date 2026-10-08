def check_name_validity(name_to_check):
    length = len(name_to_check)

    if length < 2:
        return f"Имя '{name_to_check}' слишком короткое."
    elif length > 20:
        return f"Имя '{name_to_check}' слишком длинное."
    else:
        print(f"Имя '{name_to_check}' имеет допустимую длину.")

name_to_test = ["Руслан", "Р", "Цицька", " ", "Александр Сергеевич Пушкин", "Ян"]

for name in name_to_test:
    status = check_name_validity(name)
    print(status)