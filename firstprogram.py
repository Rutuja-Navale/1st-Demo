print("ARITHMATIC OPRETORS...\n")

a =int (input("Enter a 1st number: "))
b =int (input("Enter a 2nd number: "))

print("ADDITION is= ", a+b)
print("SUBSTRACTION is= ", a-b)
print("DIVISION is= ", a/b)
print("MUTIPICATION is= ", a*b)
print("MOD is= ", a%b)

print("\n RELATIONAL OPRETORS...\n")

# equal to equal to ==
print("equal to equal to ==")
x =int (input("Enter a 1st number: "))
y =int (input("Enter a 2nd number: "))
if x == y:
    print("Numbers Are Equal\n")
else:
    print("Numbers Are Not Equal \n")
    
#Greater Than Equal to >=  
print("Greater Than Equal to >=")
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!\n")
else:
    print("You can not vote!\n")
    
#Less Than Greater Than > <
print("Less Than Greater Than <>")
p = int(input("Enter first number: "))
q = int(input("Enter second number: "))

if p > q:
    print(p,"is bigger")
else:
    print(q,"is bigger")