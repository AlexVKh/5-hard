class User:
    list_names = []

    def __new__(cls, *args):
        cls.list_names.append(args[0])
        return object.__new__(cls)

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return f'{self.nickname}'

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, title):
        return self.title == title

    def __contains__(self, search):
        return search.lower() in self.title.lower()


class UrTube():
    list_of_videos = []
    videos = []
    users = []
    current_user = None

    def __init__(self):
        pass

    def register(self, nickname, password, age):
        if nickname in User.list_names:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
        return self.users

    def log_in(self, nickname, password):
        if nickname in User.list_names:
            i = User.list_names.index(nickname)
            if hash(password) == self.users[i].password:
                self.current_user = self.users[i]
        return self.current_user

    def log_out(self):
        self.current_user = None
    def add(self, *args):
        list_ = list(args)
        for i in range(len(args)):
            if list_[i].title not in self.list_of_videos:
                self.list_of_videos.append(list_[i].title)
                self.videos.append(list_[i])
        return self.videos
    def get_videos(self,search):
        list_ = []
        for i in range(len(self.videos)):
            if search in self.videos[i]:
                list_.append(self.videos[i].title)
        return list_

    def watch_video(self, name):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if name in self.list_of_videos:
            i = self.list_of_videos.index(name)
            if self.videos[i].adult_mode == True and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            else:
                import time
                sec = 0
                while True:
                    if sec > int(self.videos[i].duration):
                        break
                    print(sec, end=' ')
                    time.sleep(1)
                    sec += 1
                print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')






