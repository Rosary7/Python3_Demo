# Exception handling
# try - except - finally
def func_convert(arg):
    try:
        return int(arg)
    except ValueError as ve:
        print("Inside except.... ")
        print("Input is not a number ", ve)
    finally:
        print("Inside finally... ")

#print(func_convert('20'))
print()
func_convert('helo')

# invalid literal for int() with base 10: 'helo'