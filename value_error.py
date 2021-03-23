day = int(input("Введите, какой сегодня день? "))

try:
    if day > 31:
        raise ValueError("Не бывает такого номера дня")
    else:
        print("Хороший денечек!")
except ValueError as msg:
    print("Program found", msg)

print(f'{day} замечательная дата')
# finally:
#     print("Have a nice day")


