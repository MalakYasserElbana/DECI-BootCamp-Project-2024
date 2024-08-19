document.getElementById('nutricare-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const age = parseInt(document.getElementById('age').value);
    const gender = document.getElementById('gender').value;
    const goal = document.getElementById('goal').value;
    const activityLevel = document.getElementById('activity-level').value;
    const dislikes = document.getElementById('dislikes').value.toLowerCase().split(',').map(item => item.trim());

    const bmi = calculateBMI(weight, height);
    const dailyCalories = calculateDailyCalories(age, weight, height, gender, activityLevel);

    const proteinNeeds = dailyCalories * 0.15 / 4;
    const fatNeeds = dailyCalories * 0.25 / 9;
    const carbNeeds = dailyCalories * 0.60 / 4;

    document.getElementById('bmi-result').innerText = `Your BMI is: ${bmi.toFixed(2)}`;
    document.getElementById('caloric-needs').innerText = `Your daily caloric needs are: ${dailyCalories.toFixed(2)} calories`;
    document.getElementById('protein-needs').innerText = `Daily protein needs: ${proteinNeeds.toFixed(2)} grams`;
    document.getElementById('fat-needs').innerText = `Daily fat needs: ${fatNeeds.toFixed(2)} grams`;
    document.getElementById('carb-needs').innerText = `Daily carbohydrate needs: ${carbNeeds.toFixed(2)} grams`;

    const mealPlan = generateMealPlan(dislikes);
    displayMealPlan(mealPlan);

    document.getElementById('results').style.display = 'block';
    document.getElementById('meal-plan').style.display = 'block';
});

function calculateBMI(weight, height) {
    return weight / ((height / 100) ** 2);
}

function calculateDailyCalories(age, weight, height, gender, activityLevel) {
    let bmr;
    if (gender === 'male') {
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age);
    } else if (gender === 'female') {
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age);
    }

    const activityFactors = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    };

    return bmr * activityFactors[activityLevel];
}

function generateMealPlan(dislikes) {
    const breakfasts = ["Oatmeal with banana and almonds", "Avocado toast with poached eggs", "Smoothie bowl with berries and granola", "Whole grain pancakes with honey", "Greek yogurt with fruit and flaxseed", "Scrambled eggs with spinach", "Chia pudding with mango"];
    const lunches = ["Grilled chicken salad with vinaigrette", "Turkey wrap with hummus and veggies", "Quinoa salad with chickpeas and feta", "Sushi rolls with brown rice", "Pasta salad with pesto and cherry tomatoes", "Lentil and vegetable stew", "Chicken and avocado sandwich"];
    const dinners = ["Baked salmon with asparagus", "Stir-fried tofu with vegetables", "Grilled steak with sweet potatoes", "Lentil soup with whole grain bread", "Chicken curry with brown rice", "Vegetable stir-fry with tofu", "Beef and broccoli stir-fry"];
    const snacks = ["Mixed nuts", "Fruit smoothie", "Veggie sticks with hummus", "Protein bar", "Cottage cheese with pineapple", "Apple slices with peanut butter", "Yogurt with honey", "Dark chocolate squares", "Rice cakes with almond butter", "Carrot sticks with ranch", "Cheese and crackers", "Popcorn", "Granola bar", "Trail mix"];

    const filteredBreakfasts = breakfasts.filter(item => !dislikes.includes(item.toLowerCase()));
    const filteredLunches = lunches.filter(item => !dislikes.includes(item.toLowerCase()));
    const filteredDinners = dinners.filter(item => !dislikes.includes(item.toLowerCase()));
    const filteredSnacks = snacks.filter(item => !dislikes.includes(item.toLowerCase()));

    if (filteredBreakfasts.length < 7 || filteredLunches.length < 7 || filteredDinners.length < 7 || filteredSnacks.length < 14) {
        return null;
    }

    const mealPlan = [];
    const daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

    for (let i = 0; i < 7; i++) {
        mealPlan.push({
            day: daysOfWeek[i],
            breakfast: filteredBreakfasts.splice(Math.floor(Math.random() * filteredBreakfasts.length), 1)[0],
            lunch: filteredLunches.splice(Math.floor(Math.random() * filteredLunches.length), 1)[0],
            dinner: filteredDinners.splice(Math.floor(Math.random() * filteredDinners.length), 1)[0],
            snack1: filteredSnacks.splice(Math.floor(Math.random() * filteredSnacks.length), 1)[0],
            snack2: filteredSnacks.splice(Math.floor(Math.random() * filteredSnacks.length), 1)[0],
        });
    }

    return mealPlan;
}

function displayMealPlan(mealPlan) {
    const mealContent = document.getElementById('meal-content');
    if (!mealPlan) {
        mealContent.innerHTML = "<p>Not enough food options to generate a unique meal plan for the week.</p>";
        return;
    }

    let mealPlanHtml = "";
    mealPlan.forEach(dayPlan => {
        mealPlanHtml += `
            <h3 class="day-name">${dayPlan.day}'s Meals:</h3>
            <p><strong>Breakfast:</strong> ${dayPlan.breakfast}</p>
            <p><strong>Lunch:</strong> ${dayPlan.lunch}</p>
            <p><strong>Dinner:</strong> ${dayPlan.dinner}</p>
            <p><strong>Snack 1:</strong> ${dayPlan.snack1}</p>
            <p><strong>Snack 2:</strong> ${dayPlan.snack2}</p>
        `;
    });

    mealContent.innerHTML = mealPlanHtml;
}

document.getElementById('new-plan').addEventListener('click', function() {
    const dislikes = document.getElementById('dislikes').value.toLowerCase().split(',').map(item => item.trim());
    const mealPlan = generateMealPlan(dislikes);
    displayMealPlan(mealPlan);
});

document.getElementById('restart').addEventListener('click', function() {
    document.getElementById('nutricare-form').reset();
    document.getElementById('results').style.display = 'none';
    document.getElementById('meal-plan').style.display = 'none';
});

document.getElementById('exit').addEventListener('click', function() {
    alert('Thank you for using NutriCare!');
    document.getElementById('nutricare-form').reset();
    document.getElementById('results').style.display = 'none';
    document.getElementById('meal-plan').style.display = 'none';
});