## exception handling


# n=10

# try:
#     res=n/0
# except ZeroDivisionError:
#     print("can't divided by zero")

# a = ["10", "twenty", 30]  # Mixed list of integers and strings
# try:
#     total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
# except (ValueError, TypeError) as e:
#     print("Error", e)
    
# except IndexError:
#     print("Index out of range.")


# def set(age):
#     if age<0:
#         raise ValueError("Age must be positive ")
#     print(f"age set to {age}")

# try:
#     set(int(input("Enter age")))
# except ValueError as e:
#     print(e)


# def check_age(age):
#     if age<18:
#         raise ValueError("Age must be 18 ")
#     return "You are eligible "

# try:
#     print(check_age(int(input("enter your age:"))))
# except ValueError as e:
#     print(f"Error {e}")



# custom exception

# class NegativeNumberError(Exception):
#     def __init__(self,message="Negative numbers are not allowed "):
#         self.message=message
#         super().__init__(self.message)
# try:
#     num=int(input("enter a number :"))
#     if num<=0:
#         raise NegativeNumberError
# except NegativeNumberError as e:
#     print(e)

def divide_num():
    try:
        num1 = int(input("Enter num1: "))  
        num2 = int(input("Enter num2: "))  
        result = num1 / num2  
    except ValueError as ve:
        print(f"Invalid input! Please enter numbers only. Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Cannot divide by zero! Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

divide_num()
