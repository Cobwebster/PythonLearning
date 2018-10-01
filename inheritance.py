class Parent():

    def print_last_name(self):
        print("Test")


class Child(Parent):

    def print_first_name(self):
        print("William")

    def print_last_name(self):
        print("Tuna")


bucky = Child()
bucky.print_last_name()