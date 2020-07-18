# Test Code to accompany the book Automating the Boring Stuff with Python

# Sample Calculator

print('Python Calculator')

num1 = input("")
operator = input("")
num2 = input("")

if operator == '+':
    print(int(num1) + int(num2))
else:
    print('Error')
