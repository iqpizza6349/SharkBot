import random

class Random_msg():
    mlist = ["❤ 청어 맛있다. ❤", "그만 주십시오💢", "☢ 체르노빌산 생선은 먹지 않습니다 ☢", "＞﹏＜ 냉동 생선은 못 먹습니다! ＞﹏＜", "🍽 맛있는 식사 시간!🍽", "o(( >ω<))o 연.어.좋.아 o((>ω< ))o"]
    result = ""

    def __init__(self, m=None):
        self.m = m
        
    def msg(self):
        temp = random.randrange(6)
        self.result = self.mlist[temp]
        return self.result