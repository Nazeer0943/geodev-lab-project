# understanding the conceept of comments, variables and data types in python
f_name = "Nazir"
s_name = "Sani"
print(f_name)
print(s_name)
p_number = 8063454567
print(p_number)
height = 5.9
print(height)
m_status = True
print(m_status)
print("The type of f_name is", type(f_name), "\ns_name is", type(s_name), "\np_number is", type(p_number), "\nheight is", type(height), "\nm_status is", type(m_status))
print("1\n2")

# The concept of lists
states = [ "Katsina", "Kano", "Kaduna", "Jigawa", "Bauchi"]
print(states)
print(states[-1])

states.append("Gombe")
print(states)

# The concept of loops, the loop/s is what prints items in an iterative manner
for state in states:
    print("We have the state of", state)

# arithmetics can also be done with the help of loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    additional_5 = number + 5
    print("The number is", number, "when 5 is added, it becomes", additional_5)
# conditional statements
for number in numbers:
    if number <= 5:
        print("This is ", number, "and it is less than or equal to 5")
    else:
        print("This is ", number, "and it is greater than 5")

# function, it is creted so that it can be used over and over without rewriting the code every time it is needed
def m_to_KM(m):
    return m / 1000

print("If 1000 meters are to be converted to KMs, it will be", m_to_KM(1000), "KMs")

# fucntions taking more than one argument
def state_and_capital(s, c):
    return "the capital of " + s + " is " + c

print(state_and_capital("Katsina", "Katsina"))