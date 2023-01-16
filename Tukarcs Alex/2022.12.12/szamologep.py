# Define a function for the calculator
def calculator(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    return "Invalid operator"

# Test the calculator function
print(calculator(1, 2, '+'))  # Should print 3
print(calculator(4, 2, '-'))  # Should print 2
print(calculator(3, 5, '*'))  # Should print 15
print(calculator(6, 2, '/'))  # Should print 3
print(calculator(5, 5, '^'))  # Should print "Invalid operator"
