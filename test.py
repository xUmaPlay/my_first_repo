# import telebot
# import requests
# import random
# import datetime
# from telebot import types
# from bs4 import BeautifulSoup
#
# bot = telebot.TeleBot("5810123187:AAGvMug4RgVzjYV1ZnTkTQTDIBumDAGVm00")
#
# value = ""
# old_value = ""
#
# keyboard = telebot.types.InlineKeyboardMarkup(row_width=4)
# keyboard.row(
#     telebot.types.InlineKeyboardButton(" ", callback_data="no"),
#     telebot.types.InlineKeyboardButton("C", callback_data="C"),
#     telebot.types.InlineKeyboardButton("<=", callback_data="<="),
#     telebot.types.InlineKeyboardButton("/", callback_data="/")
# )
#
# keyboard.row(
#     telebot.types.InlineKeyboardButton("7", callback_data="7"),
#     telebot.types.InlineKeyboardButton("8", callback_data="8"),
#     telebot.types.InlineKeyboardButton("9", callback_data="9"),
#     telebot.types.InlineKeyboardButton("*", callback_data="*")
# )
#
# keyboard.row(
#     telebot.types.InlineKeyboardButton("4", callback_data="4"),
#     telebot.types.InlineKeyboardButton("5", callback_data="5"),
#     telebot.types.InlineKeyboardButton("6", callback_data="6"),
#     telebot.types.InlineKeyboardButton("-", callback_data="-")
# )
#
# keyboard.row(
#     telebot.types.InlineKeyboardButton("1", callback_data="1"),
#     telebot.types.InlineKeyboardButton("2", callback_data="2"),
#     telebot.types.InlineKeyboardButton("3", callback_data="3"),
#     telebot.types.InlineKeyboardButton("+", callback_data="+")
# )
#
# keyboard.row(
#     telebot.types.InlineKeyboardButton(" ", callback_data="no"),
#     telebot.types.InlineKeyboardButton("0", callback_data="0"),
#     telebot.types.InlineKeyboardButton(",", callback_data="."),
#     telebot.types.InlineKeyboardButton("=", callback_data="=")
# )
#
# @bot.message_handler(commands=["calculator"])
# def getmessage(message):
#     global value
#     if value == "":
#         bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
#     else:
#         bot.send_message(message.from_user.id, value, reply_markup=keyboard)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_func(query):
#     global value, old_value
#     data = query.data
#
#     if data == "no":
#         pass
#     elif data == "C":
#         value = ""
#     elif data == "=":
#         try:
#             value = str(eval(value))
#         except:
#             value = "Ошибка!"
#     else:
#         value += data
#
#     if value != old_value:
#         if value == "":
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0", reply_markup=keyboard)
#         else:
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
#
#     old_value = value
#     if value == "Ошибка!":
#         value = ""
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     buttons = [
#         types.KeyboardButton(text="/start"),
#         types.KeyboardButton(text="/cat"),
#         types.KeyboardButton(text="/your_name"),
#         types.KeyboardButton(text="/photo"),
#         types.KeyboardButton(text="/joke"),
#         types.KeyboardButton(text="/calculator"),
#         types.KeyboardButton(text="/weather"),
#         types.KeyboardButton(text="/game"),
#         types.KeyboardButton(text="/country"),
#         types.KeyboardButton(text="/quote"),
#         types.KeyboardButton(text="/book"),
#         types.KeyboardButton(text="/rps")
#     ]
#     keyboard.add(*buttons)
#     bot.send_message(message.chat.id, "Hello! Welcome to the bot!", reply_markup=keyboard)
#
# @bot.message_handler(commands=['country'])
# def handle_country(message):
#     response = requests.get("https://api.apipip.com/v1/random-country/?format=json")
#     data = response.json()
#     country_name = data['name']
#     bot.send_message(message.chat.id, country_name)
#
# @bot.message_handler(commands=['cat'])
# def handle_cat(message):
#     bot.send_photo(message.chat.id, "https://cataas.com/cat")
#
# @bot.message_handler(commands=['book'])
# def handle_book(message):
#     url = 'http://books.toscrape.com/'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     books = soup.find_all('article', class_='product_pod')
#     book = random.choice(books)
#     book_name = book.find('h3').text
#                                                                         # book_names = [book.find('h3').text for book in books]
#                                                                         # bot.send_message(message.chat.id, random.choice(book_names))
#     bot.send_message(message.chat.id, book_name)
#
# @bot.message_handler(commands=['quote'])
# def get_random_quote(message):
#     url = 'https://quotes.toscrape.com'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     quotes = soup.find_all('span', class_='text')
#     random_quote = random.choice(quotes)
#     bot.send_message(message.chat.id, random_quote.text)
#
# @bot.message_handler(commands=['your_name'])
# def handle_your_name(message):
#     bot.send_message(message.chat.id, "aibashaibaBOT")
#
# @bot.message_handler(commands=['photo'])
# def handle_photo(message):
#     response = requests.get("https://api.thecatapi.com/v1/images/search")
#     data = response.json()
#     photo_url = data[0]['url']
#     bot.send_photo(message.chat.id, photo_url)
#
# @bot.message_handler(commands=['joke'])
# def handle_joke(message):
#     response = requests.get("https://v2.jokeapi.dev/joke/Any")
#     data = response.json()
#     if "joke" in data:
#         joke = data["joke"]
#         bot.send_message(message.chat.id, joke)
#     else:
#         bot.send_message(message.chat.id, "Failed to retrieve a joke.")
#
# @bot.message_handler(commands=['weather'])
# def handle_weather(message):
#     bot.send_message(message.chat.id, "Привет! Я бот погоды. Введите название города на английском, чтобы узнать текущую погоду.")
#     bot.register_next_step_handler(message, get_weather)
#
# def get_weather(message):
#     if message.text.lower().isalpha():
#         city = message.text.lower()
#         open_weather_token = "db6e593d88049453e3a28d44391b8a47"
#
#         code_to_smile = {
#             "Clear": "Ясно ☀️",
#             "Clouds": "Облачно ☁️",
#             "Rain": "Дождь 🌧",
#             "Drizzle": "Дождь 🌧",
#             "Thunderstorm": "Гроза ⛈",
#             "Snow": "Снег ❄️",
#             "Mist": "Туман 🌫️"
#         }
#
#         try:
#             r = requests.get(
#                 f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
#             )
#             data = r.json()
#
#             city_name = data["name"]
#             cur_weather = data["main"]["temp"]
#
#             weather_description = data["weather"][0]["main"]
#             if weather_description in code_to_smile:
#                 wd = code_to_smile[weather_description]
#             else:
#                 wd = "Посмотри в окно, не пойму что там за погода!"
#
#             humidity = data["main"]["humidity"]
#             pressure = data["main"]["pressure"]
#             wind = data["wind"]["speed"]
#             sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#             sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
#             length_of_the_day = sunset_timestamp - sunrise_timestamp
#
#             weather_message = (
#                 f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
#                 f"Погода в городе: {city_name}\nТемпература: {cur_weather}°C {wd}\n"
#                 f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
#                 f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
#                 f"Хорошего дня!"
#             )
#
#             bot.send_message(message.chat.id, weather_message)
#
#         except Exception as ex:
#             print(ex)
#             error_message = "Произошла ошибка при получении информации о погоде. Проверьте название города."
#             bot.send_message(message.chat.id, error_message)
#
# @bot.message_handler(commands=['game'])
# def handle_game(message):
#     bot.send_message(message.chat.id, "Привет! Я загадал число от 1 до 10. Попробуй угадать!")
#     bot.register_next_step_handler(message, play_game)
#
# def play_game(message):
#     if message.text.isdigit():
#         user_number = int(message.text)
#         bot_number = random.randint(1, 10)
#
#         if user_number == bot_number:
#             bot.send_message(message.chat.id, "Поздравляю! Ты угадал число!")
#         else:
#             bot.send_message(message.chat.id, f"Увы, ты не угадал. Я загадал число {bot_number}")
#     else:
#         bot.send_message(message.chat.id, "Пожалуйста, введи число от 1 до 10.")
#
# @bot.message_handler(commands=['rps'])
# def handle_start(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     buttons = [
#         types.KeyboardButton(text="/start"),
#         types.KeyboardButton(text="камень"),
#         types.KeyboardButton(text="ножницы"),
#         types.KeyboardButton(text="бумага"),
#         types.KeyboardButton(text="/rps")
#     ]
#     keyboard.add(*buttons)
#     bot.send_message(message.chat.id, "Давай сыграем в игру 'камень, ножницы, бумага'! Введи один из вариантов: камень, ножницы, бумага.", reply_markup=keyboard)
#     bot.register_next_step_handler(message, play_rps)
#
# def play_rps(message):
#     user_choice = message.text.lower()
#     bot_choice = random.choice(['камень', 'ножницы', 'бумага'])
#
#     if user_choice in ['камень', 'ножницы', 'бумага']:
#         result = get_game_result(user_choice, bot_choice)
#         response = f"Ты выбрал: {user_choice}\nЯ выбрал: {bot_choice}\n\n{result}"
#     else:
#         response = "Некорректный выбор. Пожалуйста, введи один из вариантов: камень, ножницы, бумага."
#
#     bot.send_message(message.chat.id, response)
# def get_game_result(user_choice, bot_choice):
#     if user_choice == bot_choice:
#         return "Ничья!"
#     elif (
#         (user_choice == 'камень' and bot_choice == 'ножницы') or
#         (user_choice == 'ножницы' and bot_choice == 'бумага') or
#         (user_choice == 'бумага' and bot_choice == 'камень')
#     ):
#         return "Ты победил!"
#     else:
#         return "Я победил!"
#
# @bot.message_handler(func=lambda message: True)
# def handle_invalid(message):
#     bot.send_message(message.chat.id, "Пожалуйста, введите команду '/weather' для получения погоды или '/game' для игры. '/rps' для камень ножницы бумага")
#
# bot.polling()








# import requests
#
# token = "5810123187:AAGvMug4RgVzjYV1ZnTkTQTDIBumDAGVm00"
#
# url = f"https://api.telegram.org/bot{token}/sendPhoto"
# files = {"photo": open("/home/book/photos/cat.jpg", "rb")}
# data = {"chat_id": "862486979"}
# response = requests.post(url, files=files, data=data)
# print(response.status_code)




# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
#
# posts_dict = {}  # Пустой словарь для хранения постов по userId
#
# if response.status_code == 200:
#     for post in data:
#         user_id = post["userId"]
#         if user_id in posts_dict:
#             posts_dict[user_id].append(post)
#         else:
#             posts_dict[user_id] = [post]
#
# with open('result.json', 'w') as file:
#     json.dump(posts_dict, file, indent=2)
#






# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/comments")
# data = response.json()
#
# comments_dict = {}
#
# if response.status_code == 200:
#     for comment in data:
#         post_id = comment["postId"]
#         if post_id in comments_dict:
#             comments_dict[post_id].append(comment)
#         else:
#             comments_dict[post_id] = [comment]
#
# with open('result.json', 'w') as file:
#     json.dump(comments_dict, file, indent=2)


# import requests
# import json
#
# url = 'https://jsonplaceholder.typicode.com/posts'
#
# response = requests.get(url)
# posts = response.json()
#
# user_posts = {}
#
# for post in posts:
#     user_id = post['userId']
#
#     user_posts.setdefault(user_id, [])
#
#     # if user_id not in user_posts:
#     #     user_posts[user_id] = []
#
#     user_posts[user_id].append(post)
#
# with open('result.json', 'w') as file:
#     json.dump(user_posts, file, indent=2)

# import psycopg2
# from faker import Faker
# import random
#
#
# # Функция для создания таблиц
# def create_tables():
#     conn = psycopg2.connect(
#         dbname="blog_db",
#         user="ada",
#         password="1234",
#         host="localhost",
#         port="5432"
#     )
#     conn.autocommit = True
#     cursor = conn.cursor()
#
#     # Создаем таблицу users
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100) NOT NULL,
#             email VARCHAR(100) UNIQUE NOT NULL
#         )
#     ''')
#
#     # Создаем таблицу posts
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS posts (
#             id SERIAL PRIMARY KEY,
#             title VARCHAR(100) NOT NULL,
#             content TEXT NOT NULL,
#             user_id INTEGER REFERENCES users(id)
#         )
#     ''')
#
#     # Создаем таблицу comments
#     cursor.execute('''
#             CREATE TABLE IF NOT EXISTS comments (
#                 id SERIAL PRIMARY KEY,
#                 text TEXT NOT NULL,
#                 user_id INTEGER NOT NULL,
#                 post_id INTEGER NOT NULL,
#                 FOREIGN KEY (user_id) REFERENCES users(id),
#                 FOREIGN KEY (post_id) REFERENCES posts(id)
#             )
#     ''')
#
#     conn.close()
#
#
#
# comments = [
#     'Great post!',
#     'Thanks for sharing!',
#     'I found it very useful.',
#     'Interesting news indeed.',
#     'Looking forward to more.',
#     'Well written!',
#     'You nailed it!',
#     'I agree with your points.',
#     'Very informative.',
#     'Impressive content!',
#     'This is amazing!',
#     'Keep up the good work!',
#     'You have a unique perspective.',
#     'I learned something new.',
#     'You have a talent for writing.',
#     'I enjoyed reading this.',
#     'Awesome insights!',
#     'You inspired me.',
#     'Fantastic post!',
#     'Your ideas are spot on.',
#     'This is exactly what I needed.',
#     'Keep sharing your knowledge!',
#     'You have a great writing style.',
#     'This deserves more attention.',
#     'This is a game-changer.',
#     'Thank you for sharing your expertise.',
#     'Your writing is captivating.',
#     'You have a gift for explaining complex topics.',
#     'Brilliantly written!',
#     'You made me think.',
#     'I will definitely share this.',
#     'Well-researched content.',
#     'Your post is a must-read!',
#     'I am impressed by your knowledge.',
#     'You have got a new fan!',
#     'This is so helpful.',
#     'You put things into perspective.',
#     'I cannot wait for your next post.',
#     'I will be coming back for more.',
#     'You are making a difference.',
#     'This is thought-provoking.',
#     'Excellent job!',
#     'I am sharing this with my friends.',
#     'Your insights are valuable.',
#     'You have a way with words.',
#     'I could not agree more!',
#     'This deserves to go viral.',
#     'Thank you for sharing your expertise with us.'
# ]
#
#
# # Функция для заполнения таблиц данными
# def insert_data():
#     conn = psycopg2.connect(
#         dbname="blog_db",
#         user="ada",
#         password="1234",
#         host="localhost",
#         port="5432"
#     )
#     conn.autocommit = True
#     cursor = conn.cursor()
#
#     # Вставляем данные в таблицу users
#     fake = Faker()
#     users_data = [(fake.name(), fake.email()) for _ in range(20)]
#     cursor.executemany('INSERT INTO users (name, email) VALUES (%s, %s)', users_data)
#
#     # Вставляем данные в таблицу posts
#     # Список постов для вставки
#     posts_data = [
#         (
#         'Healthy Eating Habits', 'Discover some nutritious recipes and healthy eating tips to improve your well-being.',
#         3),
#         ('Traveling on a Budget', 'Learn how to travel to your dream destinations without breaking the bank.', 2),
#         ('Technology Trends', 'Explore the latest advancements in technology and their potential impact on our lives.',
#          1),
#         ('Gardening for Beginners', 'Start your own garden and enjoy the satisfaction of growing your own plants.', 4),
#         ('Career Development Strategies', 'Useful strategies to boost your career and achieve your professional goals.',
#          5),
#         ('Art of Photography', 'Unleash your creativity with photography and capture stunning moments.', 6),
#         ('Effective Time Management', 'Master the art of time management and increase your productivity.', 7),
#         ('Mindfulness Meditation', 'Embrace mindfulness meditation to reduce stress and enhance mental clarity.', 8),
#         ('Home Organization Tips', 'Create a clutter-free and organized living space with these practical tips.', 9),
#         ('Financial Planning 101', 'Get started with financial planning and secure your financial future.', 10),
#         ('DIY Home Improvement', 'Transform your home with simple and budget-friendly DIY home improvement projects.',
#          11),
#         (
#         'Fitness and Exercise Routines', 'Stay fit and healthy with effective exercise routines and workout tips.', 12),
#         ('Fashion Trends', 'Stay updated with the latest fashion trends and style inspirations.', 13),
#         ('Delicious Dessert Recipes', 'Indulge in delightful dessert recipes that will satisfy your sweet tooth.', 14),
#         ('Pet Care Tips', 'Learn how to take care of your furry friends and keep them happy and healthy.', 15),
#         ('Learning a New Language', 'Start your language-learning journey and open doors to new cultures.', 16),
#         ('Parenting Insights', 'Discover valuable insights and advice for being a great parent.', 17),
#         (
#         'Book Recommendations', 'Find your next great read with these book recommendations from different genres.', 18),
#         ('Music and Its Impact', 'Explore the world of music and its profound impact on emotions and culture.', 19),
#         ('Inspirational Quotes', 'Get inspired by powerful quotes from influential figures and thinkers.', 20),
#         ('Cooking Adventures', 'Embark on culinary adventures and experiment with new recipes from around the world.',
#          3),
#         ('Budgeting Tips', 'Learn effective budgeting techniques to manage your finances wisely.', 4),
#         ('Web Development Basics', 'Begin your journey into web development and learn the fundamental concepts.', 5),
#         ('Yoga and Meditation',
#          'Experience the transformative power of yoga and meditation for physical and mental well-being.', 6),
#         ('Minimalist Living', 'Embrace a minimalist lifestyle and simplify your life for greater contentment.', 7),
#         ('Digital Marketing Strategies', 'Explore various digital marketing strategies to grow your online presence.',
#          8),
#         ('Declutter Your Mind', 'Discover methods to declutter your mind and achieve mental clarity.', 9),
#         ('Investing for Beginners', 'Start your investment journey and build a strong financial portfolio.', 10),
#         (
#         'Interior Design Inspiration', 'Get inspired by stunning interior design ideas to create your dream home.', 11),
#         ('Cardio Workouts', 'Engage in heart-pumping cardio workouts to stay active and healthy.', 12),
#         ('Fashionable Workwear', 'Find stylish workwear ideas to express your personality in the workplace.', 13),
#         ('Baking Delights', 'Delve into the art of baking and create delectable treats for your loved ones.', 14),
#         ('Pet Training Techniques',
#          'Learn effective pet training techniques for a harmonious relationship with your pets.', 15),
#         ('Cultural Immersion', 'Immerse yourself in different cultures and broaden your horizons.', 16),
#         ('Positive Parenting', 'Practice positive parenting techniques to nurture happy and confident children.', 17),
#         ('Science Fiction Must-Reads', 'Explore the fascinating world of science fiction with these must-reads.', 18),
#         ('Music Therapy', 'Discover the therapeutic effects of music and how it can improve well-being.', 19),
#         (
#         'Motivational Stories', 'Read inspiring stories of perseverance and determination to overcome challenges.', 20),
#         ('Photography Composition', 'Master the art of photography composition and capture captivating images.', 3),
#         ('Productivity Hacks', 'Implement productivity hacks to accomplish more in less time.', 4),
#         ('Data Science Fundamentals', 'Dive into data science and learn the foundational principles.', 5),
#         ('Mediterranean Cuisine', 'Indulge in the flavors of Mediterranean cuisine and savor delicious dishes.', 6),
#         ('Sustainable Living', 'Embrace sustainable practices to protect the environment and reduce waste.', 7),
#         ('Social Media Marketing', 'Utilize social media marketing strategies to grow your business online.', 8),
#         ('Stress Relief Techniques', 'Explore effective techniques to manage and reduce stress in your daily life.', 9),
#         ('Retirement Planning', 'Plan for a secure retirement and enjoy your golden years to the fullest.', 10),
#         ('Home Renovation Ideas', 'Get inspired by creative home renovation ideas for a fresh new look.', 11),
#         ('Strength Training', 'Build strength and muscle with effective strength training workouts.', 12),
#         ('Capsule Wardrobe Essentials', 'Curate a timeless capsule wardrobe with essential fashion pieces.', 13),
#         ('Healthy Smoothie Recipes', 'Blend delicious and nutritious smoothies for a healthy lifestyle.', 14),
#         ('Pet Health and Wellness', 'Learn about pet health and wellness to ensure the well-being of your pets.', 15),
#         ('Exploring Different Cultures', 'Embark on a journey of exploration and learn about diverse cultures.', 16),
#         ('Positive Discipline', 'Practice positive discipline techniques for effective child behavior management.', 17),
#         ('Classic Literature Classics', 'Rediscover classic literature and timeless literary works.', 18),
#         ('Music and Emotional Connection', 'Explore the emotional connection between music and the human experience.',
#          19),
#         ('Inspirational Life Lessons', 'Learn valuable life lessons from inspirational stories and experiences.', 20),
#     ]
#
#     cursor.executemany('INSERT INTO posts (title, content, user_id) VALUES (%s, %s, %s)', posts_data)
#
#     # Вставляем данные в таблицу comments
#     user_ids = list(range(1, 21))  # Пользователи имеют id от 1 до 20
#     post_ids = list(range(1, 51))  # Посты имеют id от 1 до 50
#     comments_data = []
#
#     for _ in range(250):
#         comment_text = random.choice(comments)
#         user_id = random.choice(user_ids)
#         post_id = random.choice(post_ids)
#         comments_data.append((comment_text, user_id, post_id))
#
#     cursor.executemany('INSERT INTO comments (text, user_id, post_id) VALUES (%s, %s, %s)', comments_data)
#
#     conn.close()
#
#
# if __name__ == "__main__":
#     create_tables()
#     insert_data()
