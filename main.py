# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 🚨 Don't change the code below 👇


new_size = ''

if size == 'S':
    new_size = 15
elif size == 'M':
    new_size = 20
elif size == 'L':
    new_size = 25 


if add_pepperoni == 'Y' and size == 'S':
      new_size += 2
elif add_pepperoni == 'Y':
    new_size += 3


if extra_cheese == 'Y':
    new_size += 1


print(f'Your final bill is: ${new_size}.')




