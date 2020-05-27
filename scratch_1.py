class User():
    def __init__(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id
    def describe_user(self):
        print(self.name, self.surname, self.age, self.id)
    def user_greeting(self):
        print(self.name + ", nice to see you again!")

Dima = User("Dima","Krywonos",24,"1997")
Vasya = User("Vasya","Shtefan",23,"banan")
Kolya = User("Kolya","Piwowar",22,"sztanga")

Kolya.user_greeting()
