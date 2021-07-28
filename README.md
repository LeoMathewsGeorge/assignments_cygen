# assignments_cygen

## 1. Restaurant [classes]
- Make a class called `Restaurant` . The `__init__()` method for `Restaurant` should store two attributes: a `restaurant_name` and a `cuisine_type`.
- Make a method called `describe_restaurant()` that prints these two pieces of information, and a method called `open_restaurant()` that prints a message indicating that the restaurant is open.
- Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

## 2. Number Served [classes]

- Continuing with above `Restaurant` class, add an attribute called `number_served` with a default value of `0`.
- Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
- Add a method called `set_number_served()` that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
- Add a method called `increment_number_served()` that lets you increment the number of customers who have been served. Call this method with any number you like that could represent how many customers were served in a day of business.

## 3. New type of restaurant [classes]
- An ice cream stand is a specific kind of restaurant. Write a class called `IceCreamStand` that inherits from the `Restaurant` class you wrote in above exercise. 
- Add an attribute called `flavors` that stores a list of ice cream flavors . Write a method that displays these flavors.
- Create an instance of `IceCreamStand`, and call the method to display the flavours.

## 4. Format mobile numbers [decorators]
You are given some number of mobile numbers. Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 or written before the actual digit number. Alternatively, there may not be any prefix at all.

Sample Input:
```
number_1 = 07895462130
number_2 = 919875641230
number_3 = 9195969878
```
Sample Output:
```
+91 78954 62130
+91 91959 69878
+91 98756 41230
```

- To solve the above question, make a list of the mobile numbers given and pass it to a function that sorts the list in ascending order.
- Make a decorator that standardizes the mobile numbers and apply it to the function.

## 5 Unit Tests for `Restaurant` class [testing]
- Take the `Restaurant` class you wrote in exercise 2 and Write unit tests for methods `set_number_served()` & `increment_number_served()`.
