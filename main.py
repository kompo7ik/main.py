import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyGridLayout(GridLayout):

    def calculate(self, instance):
        # Получаем значения из полей ввода
        num1 = float(self.num1.text)
        num2 = float(self.num2.text)
        num3 = float(self.num3.text)

        # Находим среднее значение
        average = (num1 + num2 + num3) / 3

        # Вычисляем модули разностей
        diff1 = abs(num1 - average)
        diff2 = abs(num2 - average)
        diff3 = abs(num3 - average)

        # Находим максимальное значение модуля разности
        max_diff = max(diff1, diff2, diff3)

        # Вычисляем результат и выводим его на экран
        result = max_diff * 100 / average
        self.result.text = str(result)


class MyApp(App):

    def build(self):
        # Создаем экземпляр GridLayout
        grid = MyGridLayout()
        grid.cols = 2

        # Создаем текстовые поля для ввода чисел
        grid.add_widget(Label(text="Число 1:"))
        grid.num1 = TextInput(multiline=False)
        grid.add_widget(grid.num1)

        grid.add_widget(Label(text="Число 2:"))
        grid.num2 = TextInput(multiline=False)
        grid.add_widget(grid.num2)

        grid.add_widget(Label(text="Число 3:"))
        grid.num3 = TextInput(multiline=False)
        grid.add_widget(grid.num3)

        # Создаем кнопку для расчета
        grid.calculate_button = Button(text="Рассчитать")
        grid.calculate_button.bind(on_press=grid.calculate)
        grid.add_widget(grid.calculate_button)

        # Создаем поле для вывода результата
        grid.add_widget(Label(text="Результат:"))
        grid.result = Label(text="")
        grid.add_widget(grid.result)

        return grid


if __name__ == "__main__":
    MyApp().run()
