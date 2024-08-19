import random

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def calculate_daily_calories(age, weight, height, gender, activity_level):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        return None
    
    activity_factors = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    
    return bmr * activity_factors.get(activity_level, None)

def get_recommendations():
    breakfasts = [
        "Oatmeal with banana and almonds",
        "Avocado toast with poached eggs",
        "Smoothie bowl with berries and granola",
        "Whole grain pancakes with honey",
        "Greek yogurt with fruit and flaxseed",
        "Scrambled eggs with spinach",
        "Chia pudding with mango"
    ]
    
    lunches = [
        "Grilled chicken salad with vinaigrette",
        "Turkey wrap with hummus and veggies",
        "Quinoa salad with chickpeas and feta",
        "Sushi rolls with brown rice",
        "Pasta salad with pesto and cherry tomatoes",
        "Lentil and vegetable stew",
        "Chicken and avocado sandwich"
    ]
    
    dinners = [
        "Baked salmon with asparagus",
        "Stir-fried tofu with vegetables",
        "Grilled steak with sweet potatoes",
        "Lentil soup with whole grain bread",
        "Chicken curry with brown rice",
        "Vegetable stir-fry with tofu",
        "Beef and broccoli stir-fry"
    ]
    
    snacks = [
        "Mixed nuts",
        "Fruit smoothie",
        "Veggie sticks with hummus",
        "Protein bar",
        "Cottage cheese with pineapple",
        "Apple slices with peanut butter",
        "Yogurt with honey",
        "Dark chocolate squares",
        "Rice cakes with almond butter",
        "Carrot sticks with ranch",
        "Cheese and crackers",
        "Popcorn",
        "Granola bar",
        "Trail mix"
    ]
    
    return breakfasts, lunches, dinners, snacks

def create_meal_plan(breakfasts, lunches, dinners, snacks, days=7):
    if len(snacks) < 2 * days:
        raise ValueError("Not enough snack options to create a unique meal plan for the week.")
    
    meal_plan = []
    
    for _ in range(days):
        daily_meals = {
            "Breakfast": breakfasts.pop(random.randrange(len(breakfasts))),
            "Lunch": lunches.pop(random.randrange(len(lunches))),
            "Dinner": dinners.pop(random.randrange(len(dinners))),
        }
        available_snacks = random.sample(snacks, 2)
        daily_meals["Snack 1"] = available_snacks[0]
        daily_meals["Snack 2"] = available_snacks[1]
        snacks.remove(available_snacks[0])
        snacks.remove(available_snacks[1])
        
        meal_plan.append(daily_meals)
    
    return meal_plan

def print_meal_plan(meal_plan):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day, meals in zip(days_of_week, meal_plan):
        print(f"\n{day}'s Meals:")
        for meal_type, meal in meals.items():
            print(f"{meal_type}: {meal}")

def get_valid_input(prompt, input_type=float):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("Welcome to NutriCare!")
        
        height = get_valid_input("Enter your height in cm: ")
        weight = get_valid_input("Enter your weight in kg: ")
        age = get_valid_input("Enter your age: ", int)
        
        while True:
            gender = input("Enter your gender (male/female): ").lower()
            if gender in ('male', 'female'):
                break
            print("Invalid input. Please enter 'male' or 'female'.")
        
        goals = {
            1: 'build muscle',
            2: 'lose weight',
            3: 'healthy living',
            4: 'maintenance'
        }
        
        while True:
            print("\nSelect your goal:")
            for number, goal in goals.items():
                print(f"{number}. {goal}")
            
            try:
                goal_choice = int(input("Enter the number corresponding to your goal: "))
                if goal_choice in goals:
                    goal = goals[goal_choice]
                    break
            except ValueError:
                pass
            print("Invalid input. Please enter a valid number corresponding to a goal.")
        
        activity_levels = {
            1: 'sedentary',
            2: 'light',
            3: 'moderate',
            4: 'active',
            5: 'very active'
        }
        
        while True:
            print("\nSelect your activity level:")
            for number, level in activity_levels.items():
                print(f"{number}. {level}")
            
            try:
                activity_choice = int(input("Enter the number corresponding to your activity level: "))
                if activity_choice in activity_levels:
                    activity_level = activity_levels[activity_choice]
                    break
            except ValueError:
                pass
            print("Invalid input. Please enter a valid number corresponding to an activity level.")
        
        dislikes = input("\n(1)Are there any foods you dislike or are allergic to? (comma-separated, If no type 'none'): ").lower()
        if dislikes.strip() == "none":
            dislike_list = []
        else:
            dislike_list = [item.strip() for item in dislikes.split(',') if item.strip()]

        bmi = calculate_bmi(weight, height)
        daily_calories = calculate_daily_calories(age, weight, height, gender, activity_level)
        
        if daily_calories is None:
            print("An error occurred while calculating daily caloric needs. Please check your inputs.")
            return
        
        protein_needs = daily_calories * 0.15 / 4
        fat_needs = daily_calories * 0.25 / 9
        carb_needs = daily_calories * 0.60 / 4
        
        print("\n(2)Your BMI is: {:.2f}".format(bmi))
        print("Your daily caloric needs are: {:.2f} calories".format(daily_calories))
        print("Daily protein needs: {:.2f} grams".format(protein_needs))
        print("Daily fat needs: {:.2f} grams".format(fat_needs))
        print("Daily carbohydrate needs: {:.2f} grams".format(carb_needs))
        
        breakfasts, lunches, dinners, snacks = get_recommendations()
        
        filtered_breakfasts = [food for food in breakfasts if not any(dislike in food.lower() for dislike in dislike_list)]
        filtered_lunches = [food for food in lunches if not any(dislike in food.lower() for dislike in dislike_list)]
        filtered_dinners = [food for food in dinners if not any(dislike in food.lower() for dislike in dislike_list)]
        filtered_snacks = [food for food in snacks if not any(dislike in food.lower() for dislike in dislike_list)]
        
        if len(filtered_breakfasts) < 7 or len(filtered_lunches) < 7 or len(filtered_dinners) < 7 or len(filtered_snacks) < 14:
            print("Not enough food options to generate a unique meal plan for the week.")
            return
        
        print("\n(3)Generating a 7-day meal plan...")
        meal_plan = create_meal_plan(filtered_breakfasts, filtered_lunches, filtered_dinners, filtered_snacks)
        print_meal_plan(meal_plan)
        
        # Offer to restart or generate a new meal plan
        while True:
            print("\nOptions:")
            print("1. Generate a new meal plan")
            print("2. Restart the process")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                print("\nGenerating a new meal plan with the same settings...")
                meal_plan = create_meal_plan(filtered_breakfasts, filtered_lunches, filtered_dinners, filtered_snacks)
                print_meal_plan(meal_plan)
                break
            elif choice == '2':
                print("\nRestarting the process...\n")
                break
            elif choice == '3':
                return
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()