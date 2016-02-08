class NonPositiveInputError(Exception):
    def __init__(self, expr="", msg=""):
        self.expr = expr
        self.msg = msg
try:
    my_list = [1,2,3,5]
    number = int(input("What item number in the list should i read? "))
    if number <= 0:
        raise NonPositiveInputError
    x = my_list[number-1]
    print(x)
except IndexError:
    print("Sorry, this list contains", len(my_list),"items. You requested item number", number)
except ValueError:
    print("You need to enter a valid number. Make sure not to have any spaces or decimal points. The number should not be zero or negative.")
except NonPositiveInputError:
    print("Needs to be a positive, non-zero number")
