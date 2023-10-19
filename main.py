#1
import random
def roll_dice():
    result = random.randint(1,6)
    result = int(result)
    return result
roll = input("Do you want to roll dice? (y/n) ")
if roll == "n":
    print("Thanks for playing.")
while roll == "y":
    dice_result = roll_dice()
    dice_result= int(dice_result)
    if dice_result == 6:
        print("You rolled a 6!")
        break
    elif roll == "n":
        print("Thanks for playing.")
    else:
        print(f"Result of your roll: {dice_result}")
        roll = input("Do you want to roll? (y/n) ")
        if roll == "n":
            print("Thanks for playing.")

#2
import random
def roll_dice(sides):
    return random.randint(1, sides)
max_number = int(input("Enter the maximum number on the dice: "))

rolls = 0
result = 0
while result != max_number:
    rolls += 1
    result = roll_dice(max_number)
    print(f"Roll {rolls}: {result}")

print(f"You rolled the maximum number: {max_number}!")


#3
def convert_gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
gallons = 0
while gallons >= 0:
    gallons = float(input("Enter a volume in American gallons (or a negative value to quit): "))
    if gallons >= 0:
        liters = convert_gallons_to_liters(gallons)
        print(f"{gallons:.2f} gallons is equal to {liters:.2f} liters.")

#4
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
num_list = [1, 2, 3, 4, 5]
result = calculate_sum(num_list)
print("Sum of the numbers:", result)

#5
def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_odd_numbers(num_list)
print("Original list:", num_list)
print("Filtered list (even numbers only):", filtered_list)


#6
def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = 3.14159 * (radius ** 2)
    area_m2 = area_cm2 / 10000
    unit_price = price / area_m2
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza (in centimeters): "))
price1 = float(input("Enter the price of the first pizza (in euros): "))

diameter2 = float(input("Enter the diameter of the second pizza (in centimeters): "))
price2 = float(input("Enter the price of the second pizza (in euros): "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas have the same unit price.")









