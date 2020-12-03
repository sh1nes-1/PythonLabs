from tkinter import *

class Form:
    def __init__(self, parent):
        Label(parent, width=20, text=' Перше число:', pady=10).pack()
        self.entry1 = Entry(parent, width=20)
        self.entry1.pack()

        Label(parent, width=20, text='Друге число:', pady=10).pack()
        self.entry2 = Entry(parent, width=20)
        self.entry2.pack()

        self.multiply = BooleanVar()
        Radiobutton(parent, width=10, text="Добуток", pady=10, variable=self.multiply, value=1).pack()
        Radiobutton(parent, width=10, text="Частка", pady=10, variable=self.multiply, value=0).pack()

        self.calcBtn = Button(parent, text="Порахувати", pady=10)
        self.calcBtn['command'] = self.calculate
        self.calcBtn.pack()

        self.resultLabel = Label(parent, width=40, pady=20, text='Результат:')
        self.resultLabel.pack()

    def calculate(self):
        val1 = self.entry1.get()
        val2 = self.entry2.get()
        isMultiply = self.multiply.get()

        if not val1 or not val2:
            self.resultLabel['text'] = 'Поля є обов\'язковими'
            return

        if not val1.isnumeric() or not val2.isnumeric():
            self.resultLabel['text'] = 'Поля мають містити лише числа'
            return

        num1 = int(val1)
        num2 = int(val2)

        if isMultiply:
            result = num1 * num2
            self.resultLabel['text'] = f'Результат: {result}'
            return

        if num2 == 0:
            self.resultLabel['text'] = 'Ділення на нуль не підтримується'
            return

        result = num1 / num2
        self.resultLabel['text'] = f'Результат: {result}'

root = Tk()
root.title('Варіант 14')
root.resizable(False, False)

main = Form(root)

root.mainloop()