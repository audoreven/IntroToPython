import bytework

class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Error: %s" % self.value


try:
    raise CustomError("something went wrong")

except CustomError as e:
    print(e)


dict = {}

dict[1234] = "hello there I am boreed"

print(dict[4321])

acc = bytework.Account