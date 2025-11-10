# --------------------------------------------
# Name: Arnav Kapil
# Date: 10 Nov 2025
# Project: Daily Calorie Tracker (Mini Project)
# --------------------------------------------

print("Welcome to the Daily Calorie Tracker!")
print("This program helps you record your meals and track total calories.\n")

# Task 2: Input & Data Collection
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"Enter meal #{i+1} name: ")
    meal_cal = float(input(f"Enter calories for {meal_name}: "))
    
    meals.append(meal_name)
    calories.append(meal_cal)

# Task 3: Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / num_meals

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    print("\n⚠️ You have exceeded your daily calorie limit!")
else:
    print("\n✅ You are within your daily calorie limit. Great job!")

# Task 5: Neatly Formatted Output
print("\n------ Daily Calorie Summary ------")
print("Meal Name\tCalories")
print("------------------------------")

for i in range(num_meals):
    print(f"{meals[i]}\t\t{calories[i]}")

print("------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

# Task 6 (Bonus): Save Session Log to File
save_choice = input("\nDo you want to save this session? (yes/no): ").lower()

if save_choice == "yes":
    with open("calorie_log.txt", "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write("------------------------------\n")
        for i in range(num_meals):
            file.write(f"{meals[i]}\t{calories[i]}\n")
        file.write("------------------------------\n")
        file.write(f"Total Calories: {total_calories}\n")
        file.write(f"Average Calories: {average_calories:.2f}\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded Limit ⚠️\n")
        else:
            file.write("Status: Within Limit ✅\n")
    print("Your session has been saved to 'calorie_log.txt'.")

print("\nThank you for using the Daily Calorie Tracker!")
