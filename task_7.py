import random
import matplotlib.pyplot as plt

# Аналітичні ймовірності для кожної суми
analytical_probabilities = {
    2: (1, 36), 3: (2, 36), 4: (3, 36), 5: (4, 36), 6: (5, 36), 7: (6, 36),
    8: (5, 36), 9: (4, 36), 10: (3, 36), 11: (2, 36), 12: (1, 36)
}

# Функція для моделювання кидків кубиків
def monte_carlo_simulation(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}  # Словник для підрахунку сум

    # Моделюємо кидки кубиків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sum_of_dice = die1 + die2
        sum_counts[sum_of_dice] += 1

    # Обчислення ймовірностей
    probabilities = {sum_value: (count / num_rolls) * 100 for sum_value, count in sum_counts.items()}

    return probabilities


def main():
    # Користувач вводить кількість кидків кубиків
    try:
        num_rolls = int(input("Введіть кількість кидків кубиків: "))
        if num_rolls <= 0:
            print("Кількість кидків повинна бути більшою за 0!")
            return
    except ValueError:
        print("Будь ласка, введіть коректне число!")
        return

    # Симуляція за допомогою методу Монте-Карло
    mc_probabilities = monte_carlo_simulation(num_rolls)

    # Виведення ймовірностей у вигляді таблиці
    print(f"\n{'Сума':<18} {'Імовірність'}")
    print("-" * 38)

    for sum_value in range(2, 13):
        mc_prob = mc_probabilities[sum_value]
        analytical_num, analytical_den = analytical_probabilities[sum_value]
        analytical_prob = (analytical_num / analytical_den) * 100
        print(f"{sum_value:<18} {mc_prob:.2f}% ({analytical_num}/{analytical_den})")

    # Побудова графіка
    sums = list(range(2, 13))
    mc_probs = [mc_probabilities[sum_value] for sum_value in sums]
    analytical_probs = [(analytical_num / analytical_den) * 100 for sum_value in sums for analytical_num, analytical_den in [analytical_probabilities[sum_value]]]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_probs, alpha=0.6, label="Монте-Карло")
    plt.plot(sums, analytical_probs, 'ro-', label="Аналітичні ймовірності")
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title(f'Ймовірності сум при киданні двох кубиків ({num_rolls} кидків)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()