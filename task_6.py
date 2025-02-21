# Словник зі стравами, їх вартістю та калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Функція жадібного алгоритму
def greedy_algorithm(budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    items_with_ratio = []
    for item, values in items.items():
        cost = values["cost"]
        calories = values["calories"]
        ratio = calories / cost
        items_with_ratio.append((item, cost, calories, ratio))

    # Сортуємо страви за співвідношенням калорій до вартості у порядку спадання
    items_with_ratio.sort(key=lambda x: x[3], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    # Додаємо страви, поки не перевищимо бюджет
    for item, cost, calories, _ in items_with_ratio:
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories


# Функція динамічного програмування
def dynamic_programming(budget):
    n = len(items)
    dp = [0] * (budget + 1)  # Массив для збереження максимальних калорій для кожного бюджету
    selected_items = [[] for _ in range(budget + 1)]  # Масив для збереження страв для кожного бюджету

    # Створюємо список страв
    items_list = [(item, values["cost"], values["calories"]) for item, values in items.items()]

    # Проходимо по кожному можливому бюджету
    for item, cost, calories in items_list:
        for b in range(budget, cost - 1, -1):
            if dp[b] < dp[b - cost] + calories:
                dp[b] = dp[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [item]

    # Вибираємо набір страв для максимального бюджету
    return selected_items[budget], dp[budget]


# Основна частина програми
def main():
    # Запитуємо у користувача бюджет
    budget = int(input("Введіть свій бюджет: "))
    
    # Жадібний алгоритм
    greedy_items, greedy_calories = greedy_algorithm(budget)
    print("\nЖадібний алгоритм:")
    print("Вибрані страви:", greedy_items)
    print("Загальна калорійність:", greedy_calories)

    # Алгоритм динамічного програмування
    dp_items, dp_calories = dynamic_programming(budget)
    print("\nАлгоритм динамічного програмування:")
    print("Вибрані страви:", dp_items)
    print("Загальна калорійність:", dp_calories)

# Викликаємо основну функцію
if __name__ == "__main__":
    main()