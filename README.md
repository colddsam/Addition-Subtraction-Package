 # Python Class for Dynamically Switching Between Addition and Subtraction Operations: AddSub

---

## Introduction

In this tutorial, we will create a Python class named `AddSub` that allows us to dynamically switch between addition and subtraction operations. This class provides a flexible way to perform different operations on numbers based on a specified method.

## Code Implementation

```python
class AddSub:
    def __init__(self, method_val: int = 1) -> None:
        """
        This is the constructor of the AddSub class.
        It takes an optional parameter method_val, which specifies the default method to be used for operations.
        If method_val is not an integer, it is set to 1 (addition) by default.
        If method_val is less than 0 or greater than 1, it is also set to 1 by default.
        """

        if type(method_val) != type(1):
            self.method = 1
            print('only integer elements accepted')
        elif ((method_val <= 1) and (method_val >= 0)):
            self.method = method_val
        else:
            self.method = 1
            print("Please enter a valid method by default addition operation has set")

    def operation(self, first_number: int = 0, second_number: int = 0) -> int:
        """
        This method performs the operation specified by the method attribute on the two given numbers.
        If the method attribute is 0, subtraction is performed.
        If the method attribute is 1, addition is performed.
        """

        if (self.method == 0):
            return first_number - second_number
        elif (self.method == 1):
            return first_number + second_number

    def change_method(self, method_val: int) -> None:
        """
        This method changes the method attribute to the given value.
        If the given value is not an integer, the method attribute is not changed.
        If the given value is less than 0 or greater than 1, the method attribute is also not changed.
        """

        if (type(method_val) != type(1)):
            print('only integer elements accepted, previous method has unchanged')
        elif ((method_val <= 1) and (method_val >= 0)):
            self.method = method_val
        else:
            print("Please enter a valid method, previous method has unchanged")


# Usage:

# Creating an instance of the AddSub class
add_sub = AddSub()

# Performing addition using the default method
result = add_sub.operation(10, 20)
print("Addition result:", result)  # Output: 30

# Changing the method to subtraction
add_sub.change_method(0)

# Performing subtraction using the new method
result = add_sub.operation(20, 10)
print("Subtraction result:", result)  # Output: 10

# Changing the method to an invalid value
add_sub.change_method(2)

# Performing addition using the previous method (addition)
result = add_sub.operation(100, 200)
print("Addition result (using previous method):", result)  # Output: 300
```

## Explanation

1. The `__init__` method is the constructor of the `AddSub` class. It takes an optional parameter `method_val` that specifies the default method to be used for operations.
2. In the `__init__` method, we check if `method_val` is an integer. If it is not, we print an error message and set `method` to 1 (addition).
3. We also check if `method_val` is within the valid range of 0 (subtraction) and 1 (addition). If it is not, we print an error message and set `method` to 1.
4. The `operation` method takes two integer parameters `first_number` and `second_number` and performs the operation specified by the `method` attribute on the two given numbers.
5. The `change_method` method takes an integer parameter `method_val` and changes the `method` attribute to the given value, provided that it is a valid value.
6. In the usage section, we create an instance of the `AddSub` class and perform addition and subtraction operations using the default method.
7. We then change the method to subtraction using the `change_method` method and perform a subtraction operation.
8. We try to change the method to an invalid value, but the `change_method` method prevents this and prints an error message.
9. Finally, we perform an addition operation using the previous method (addition) and demonstrate that the method has not changed.

## Conclusion

The `AddSub` class provides a flexible way to dynamically switch between addition and subtraction operations. This can be useful in various scenarios where you need to perform different operations based on certain conditions or user input.