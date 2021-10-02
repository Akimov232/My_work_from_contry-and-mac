class Person:
    def __init__(self, first_name, last_name):
        self.first = str(first_name)
        self.last = str(last_name)

    def speak(self):
        print(f"My name is " + self.first + " " + self.last)


me = Person("Olli", "Green")
you = Person("Tommy", "Wiseau")

me.speak()
you.speak()