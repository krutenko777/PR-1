#Задание 1
# import random
#
# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def play_random_track(self):
#         random_track_index = random.randint(0, len(self.tracklist) - 1)
#         print("Название:", self.title)
#         print("Исполнитель:", self.artist)
#         print("Год:", self.release_year)
#         print("Жанр:", self.genre)
#         print("Треки:", self.tracklist)
#         print("Воспроизводится трек {}: {}".format(random_track_index + 1, self.tracklist[random_track_index]))
#
# album = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte", ['Deutschland', 'Radio', 'Zeigdich', 'Ausländer', 'Sex', 'Puppe', 'Wasichliebe', 'Diamant', 'Weitweg', 'Tattoo', 'Hallomann'])
#
# album.play_random_track()

#Задание 2
# from statistics import mean
# class Student:
#      def __init__(self, name, age, grade, scores):
#          self.name = name
#          self.age = age
#          self.grade = grade
#          self.scores = scores
#
#      def print_all(self):
#          print(f'Имя: {self.name}\n'
#                f'Возраст: {self.age}\n'
#                f'Класс: {self.grade}\n'
#                f'Оценки: {self.scores}')
#
#      def average_score(self):
#          avg_score = mean(self.scores)
#          print(f'Средний балл: {avg_score}')
# egor = Student("Егор Данилов", "12", "5В", [5, 4, 4, 5])
# egor.print_all()
# egor.average_score()

#Задание 3
# class Recipe:
#
#      def __init__(self, name, recipe):
#          self.name = name
#          self.recipe = recipe
#
#      def print_ingredients(self):
#          print(f'Ингридиенты для {self.name}:')
#          for i in range (len(self.recipe)):
#              print(f'- {self.recipe[i]}')
#
#      def cook(self):
#          print(f'Выполняем инструкцию по приготовлению блюда {self.name}...\n'
#                f'Блюдо {self.name} готово!')
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()