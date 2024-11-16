# import threading as th

# def count(end):
#     for i in range(end):
#         print(i)
#     print(f"Завершено {end}")

# def letters(word):
#     for i in word:
#         print(i)
#     print(f"{word}  завершено")

# thread1 = th.Thread(target=count,args=(15,))
# thread2 = th.Thread(target=letters,args=("hello world!!!",))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


class Character:
    def __init__(self, xp, st, mp):
        self.xp = xp
        self.st = st
        self.mp = mp 
    def getInfo(self):
        return f"xp = {self.xp} st = {self.st } mp = {self.mp}"
