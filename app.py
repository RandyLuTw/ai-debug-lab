def add(a, b):
    return a + b


first_input = input("請輸入第一個數字: ")
second_input = input("請輸入第二個數字: ")

try:
    first_number = float(first_input)
    second_number = float(second_input)
    result = add(first_number, second_number)
    print("相加結果是:", result)
except ValueError:
    print("錯誤：請輸入有效的數字。")
