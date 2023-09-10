import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import program


class MainWindow(QtWidgets.QMainWindow, program.Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.numbers_place_string = ""
        self.n_1 = ""
        self.action = ""
        self.action_list = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b,
                            "/": lambda a, b: a / b, "//": lambda a, b: a // b, "%": lambda a, b: a % b,
                            "**": lambda a, b: a ** b, "sq": lambda a, b: a ** 0.5}

        self.symbols = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

        self.number_0.pressed.connect(self.pressed_0)
        self.number_1.pressed.connect(self.pressed_1)
        self.number_2.pressed.connect(self.pressed_2)
        self.number_3.pressed.connect(self.pressed_3)
        self.number_4.pressed.connect(self.pressed_4)
        self.number_5.pressed.connect(self.pressed_5)
        self.number_6.pressed.connect(self.pressed_6)
        self.number_7.pressed.connect(self.pressed_7)
        self.number_8.pressed.connect(self.pressed_8)
        self.number_9.pressed.connect(self.pressed_9)
        self.clear.pressed.connect(self.clear_string)
        self.backspace.pressed.connect(self.backspace_string)
        self.make_float.pressed.connect(self.append_period)
        self.plus.pressed.connect(self.plus_action)
        self.minus.pressed.connect(self.minus_action)
        self.multiply.pressed.connect(self.multiply_action)
        self.standart_division.pressed.connect(self.standart_division_action)
        self.remains_division.pressed.connect(self.remains_division_action)
        self.integer_division.pressed.connect(self.integer_division_action)
        self.power.pressed.connect(self.power_action)
        self.square_root.pressed.connect(self.square_root_action)
        self.equally.pressed.connect(self.equally_action)
        self.from_dec.pressed.connect(self.from_dec_action)
        self.in_dec.pressed.connect(self.in_dec_action)

    def dec(func):
        def fun(self, *args, **kwargs):
            try:
                self.numbers_place_string = self.numbers_place.toPlainText()
                func(self, *args, **kwargs)
            except ZeroDivisionError:
                self.numbers_place.setText("На 0 делить нельзя")
            except Exception as exception:
                self.numbers_place.setText("Error")
                print(exception)

        return fun

    @dec
    def append_number(self, number="0"):
        self.numbers_place_string += number
        self.numbers_place.setText(self.numbers_place_string)

    def pressed_0(self):
        self.append_number("0")

    def pressed_1(self):
        self.append_number("1")

    def pressed_2(self):
        self.append_number("2")

    def pressed_3(self):
        self.append_number("3")

    def pressed_4(self):
        self.append_number("4")

    def pressed_5(self):
        self.append_number("5")

    def pressed_6(self):
        self.append_number("6")

    def pressed_7(self):
        self.append_number("7")

    def pressed_8(self):
        self.append_number("8")

    def pressed_9(self):
        self.append_number("9")

    def clear_string(self):
        self.n_1 = ""
        self.action = ""
        self.numbers_place.setText("")

    @dec
    def backspace_string(self):
        self.numbers_place_string = self.numbers_place_string[:-1]
        self.numbers_place.setText(self.numbers_place_string)

    @dec
    def append_period(self):
        if "." not in self.numbers_place_string:
            self.numbers_place_string += "."
            self.numbers_place.setText(self.numbers_place_string)

    def plus_action(self):
        self.sign_action("+")

    def minus_action(self):
        self.sign_action("-")

    def standart_division_action(self):
        self.sign_action("/")

    def integer_division_action(self):
        self.sign_action("//")

    def remains_division_action(self):
        self.sign_action("%")

    def multiply_action(self):
        self.sign_action("*")

    def power_action(self):
        self.sign_action("**")

    @dec
    def square_root_action(self):
        sq_number = float(self.numbers_place_string)
        sq_number = sq_number ** 0.5
        self.numbers_place.setText(str(sq_number))

    @dec
    def from_dec_action(self):
        n = float(self.numbers_place_string) if self.numbers_place_string.isdigit() else 0.0
        s = float(self.system_place.toPlainText()) if self.system_place.toPlainText().isdigit() and 2 <= float(self.system_place.toPlainText()) <= 16 else 0.0
        n_s = ""
        while n >= s:
            symbol = str(n % s)
            if int(symbol) > 9:
                symbol = self.symbols[symbol]
            n_s += symbol
            n = n // s
        n_s += str(n)
        self.numbers_place.setText("".join(list(reversed(list(n_s)))))

    @dec
    def in_dec_action(self):
        n = float(self.numbers_place_string) if self.numbers_place_string.isdigit() else 0.0
        s = float(self.system_place.toPlainText())
        n = [(float(symbol[1]), symbol[0]) for symbol in enumerate("".join(list(reversed(list(str(n))))))]
        self.numbers_place.setText(str(sum([x[0] * s ** float(x[1]) for x in n])))

    @dec
    def sign_action(self, sign):
        if self.n_1 and self.action:
            self.n_1 = str(self.action_list[self.action](float(self.n_1), float(self.numbers_place_string)))
        else:
            self.n_1 = self.numbers_place_string
        self.action = sign
        self.numbers_place.setText("")

    @dec
    def equally_action(self):
        self.numbers_place.setText(str(self.action_list[self.action](float(self.n_1), float(self.numbers_place_string))))
        self.action = ""
        self.n_1 = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec_())
