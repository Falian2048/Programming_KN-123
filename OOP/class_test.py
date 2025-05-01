from rich import print
'''Якщо виконувати программу в консолі Windows або увімкнути емулювання терміналу в налаштуваннях Run/Debug configuration буде краще'''


class Cat:
    def __init__(self, name="[bold red][Default name][/bold red]", age=0, color="[bold red][Default color][/bold red]", sound="Мяу"):
        self.name = name
        self.age = age
        self.color = color
        self.sound = sound
        print(f"Котик {self.name}, якому {self.age}, має {self.color} колір -- створений")

    def speak(self):
        print(f"Ваш {self.color} котик {self.name} сказав: [bold]{self.sound}[/bold]")

print("Вітаю! Зараз Ви зможете створити свого котика)")
name = input("Як будуть звати Вашого котика: ")
age = input("Скільки йому/їй років: ")
color = input("Якого він/вона кольору: ")
sound = input("Що каже котик: ")
cat = Cat(name if name else "[bold red][Default name][/bold red]", age if age else 0, color if color else "[bold red][Default color][/bold red]", sound if sound else "мяу")
cat.speak()