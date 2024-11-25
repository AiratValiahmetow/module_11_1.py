import matplotlib.pyplot as plt

# Данные для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y, marker='o')
plt.title('Пример графика')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

# Отображение графика
plt.show()


# import requests
#
# # Получение данных с веб-сайта
# response = requests.get('https://api.github.com')
# data = response.json()
#
# # Вывод данных в консоль
# print(data)
