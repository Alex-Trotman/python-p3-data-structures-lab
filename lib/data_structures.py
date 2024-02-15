spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food['name'])

    return names
        

def get_spiciest_foods(spicy_foods):
    spiciest = []

    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest.append(food)

    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_str = "🌶" * food['heat_level']

        food_str = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_str}"

        print(food_str)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    def heat_level_emoji(heat_level):
        return "🌶" * heat_level

    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = heat_level_emoji(food["heat_level"])
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 for an empty list to avoid division by zero

    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)
    
    average_heat = total_heat_level / num_spicy_foods
    return int(average_heat)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
