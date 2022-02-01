class ComplexNumberException(Exception):
  pass

class TooBigNumberException(Exception):
  pass

class TooSmallNumberException(Exception):
  pass

class NegativeNumberException(Exception):
  pass

def cast_to_float(input):
    # If input is a complex number, raise a ComplexNumberException
    if "j" in input:
        raise ComplexNumberException()

    # If input is a negative number, raise a NegativeNumberException
    if input[0] == "-":
        raise NegativeNumberException()

    # If input has more than 16 digits, raise a TooBigNumberException
    if len(input) > 9:
        raise TooBigNumberException()

    # If input value is less than 0.01, raise a TooSmallNumberException
    if abs(float(input)) < 0.01:
        raise TooSmallNumberException()

    # Cast the input in int for any other case
    return float(input)

def get_user_input(message):
    finished = False
    value = ""

    # The program keep looping until the user
    # inputs acceptable values
    while finished == False:
        value = str(input(message))
        try:
            value = cast_to_float(value)
            # Set finished to True to leave the while loop 
            finished = True

        except NegativeNumberException:
            print("Numbers should be positive")
            print("The value will be turned into a positive value")
            value = float(value)*-1
            # Set finished to True to leave the while loop 
            # and exit the program
            finished = True

        except ComplexNumberException:
            print("Complex numbers cannot be casted to int")
            print("The real part of the number will be casted to int")

            # If the cast to complex couldn't be done (space between +/- or inversion of the real and immaginary part)
            # The user will be asked to input another number
            try:
                value = complex(value).real
                finished = True
            except:
                print("The complex number was not properly formed")
                print("Please input another number")
                # Set finished to True to leave the while loop 
                # and exit the program

        except TooBigNumberException:
            print("Numbers having more than 16 digits cannot be used")
            print("Please select another value")

        except TooSmallNumberException:
            print("Numbers being too small cannot be used")
            print("Please select another value")

    return value  

def polynome(x):
    result = (x**3 - 1.5*(x**2) - 6*x + 5)
    return result

if __name__ == '__main__':
    x = get_user_input("Enter the value of x: ")
    result = polynome(x)
    print(result)
    

