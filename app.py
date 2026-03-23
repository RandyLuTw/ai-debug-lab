def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    try:
        a = float(input("請輸入第一個數字: "))
        b = float(input("請輸入第二個數字: "))
    except ValueError:
        print("錯誤：請輸入有效的數字。")
        return

    operation = input("請選擇運算（+ 或 -）: ").strip()

    if operation == "+":
        result = add(a, b)
        print("加法結果是:", result)
    elif operation == "-":
        result = subtract(a, b)
        print("減法結果是:", result)
    else:
        print("錯誤：請輸入 + 或 -。")


if __name__ == "__main__":
    main()
