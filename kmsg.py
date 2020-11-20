import random

class kmsg():
    kmsg = ["회로 썰어주지", "매운탕? 좋지~", "나의 소중한 간식거리겠구먼", "뭘 봐, 네 친구야", "썩 좋은 삶이였다!"]
    result = ""

    def __init__(self, m=None):
        self.m = m

    def msg(self):
        temp = random.randrange(4)
        self.result = self.kmsg[temp]
        return self.result