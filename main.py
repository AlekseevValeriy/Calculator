class Calculator:
    def __init__(self):
        self.actions = {"сложение": self.plus, "вычитание": self.minus, "умножение": self.multiply,
                        "деление": self.standart_division, "целочисленное деление": self.integer_division,
                        "остаток от деления": self.remains_division, "степень": self.power, "корень": self.square_root,
                        "с десятичной": self.from_dec, "в десятичную": self.in_dec, "выйти": self.exit,
                        "информация": self.actions_information}
        self.process_flag = True
        self.symbols = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

    def plus(self, n_1, n_2):
        return n_1 + n_2

    def minus(self, n_1, n_2):
        return n_1 - n_2

    def multiply(self, n_1, n_2):
        return n_1 * n_2

    def standart_division(self, n_1, n_2):
        try:
            return n_1 / n_2
        except ZeroDivisionError:
            return "На 0 делить нельзя"

    def integer_division(self, n_1, n_2):
        try:
            return n_1 // n_2
        except ZeroDivisionError:
            return "На 0 делить нельзя"

    def remains_division(self, n_1, n_2):
        try:
            return n_1 % n_2
        except ZeroDivisionError:
            return "На 0 делить нельзя"

    def power(self, n_1, n_2):
        return n_1 ** n_2

    def square_root(self, n):
        return int(n) ** 0.5

    def in_dec(self, n_s):
        n, s = map(int, n_s.split())
        n = [(int(symbol[1]), symbol[0]) for symbol in enumerate("".join(list(reversed(list(str(n))))))]
        return sum([x[0] * s ** x[1] for x in n])

    def from_dec(self, n_s):
        n, s = map(int, n_s.split())
        n_s = ""
        while n >= s:
            symbol = str(n % s)
            if int(symbol) > 9: symbol = self.symbols[symbol]
            n_s += symbol
            n = n // s
        n_s += str(n)
        return "".join(list(reversed(list(n_s))))

    def exit(self):
        self.process_flag = False

    def actions_information(self):
        print(
            "сложение - 2 числа\nвычитание - 2 числа\nумножение - 2 числа\nделение - 2 числа\nцелочисленное деление - 2 числа\nостаток от деления - 2 числа\nстепень - 2 числа\nкорень - 1 число\nс десятичной - 1 строка(число пробел система счисления)\nв десятичную - 1 строка(число пробел система счисления)\nвыйти - None\nинформация - None", "\n")

    def main_process(self):
        while self.process_flag:
            action = input("Введите действие:", ).rstrip().lstrip().lower()
            if action not in self.actions:
                print("Введите корректное действие", "\n")
                continue
            if action in ["выйти", "информация"]:
                self.actions[action]()
                continue
            try:
                number_1 = input("Первое число:", ).rstrip().lstrip()
                if action in ["корень", "в десятичную", "с десятичной"]:
                    print(self.actions[action](number_1), "\n")
                    continue
                number_2 = int(input("Второе число:", ).rstrip().lstrip())
                print(self.actions[action](number_1, number_2), "\n")
            except Exception as exception:
                print(exception)
                print("Введите корректные значения", "\n")
                continue


if __name__ == '__main__':
    calculator = Calculator()
    calculator.main_process()
