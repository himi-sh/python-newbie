
class MyException(Exception):
    def __init__(self, message):
        print("Inside init method")
        self.message = message

try:
    raise MyException("calling init method")
except MyException as ex:
    print("Inside except => ", ex.message)