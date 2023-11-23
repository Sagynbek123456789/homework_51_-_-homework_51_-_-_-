import random
CAT_AVATAR_LEVEL_HAPPINESS_GT_60 = '/img/img-2.jpg'
CAT_AVATAR_LEVEL_HAPPINESS_GT_30_OR_LT_60 = '/img/img-3.jpg'
CAT_AVATAR_LEVEL_HAPPINESS_LT_30 = '/img/img-1.jpg'


class Cat:
    name = ''
    age = 1
    is_sleeping = False
    satiety = 40
    happiness = 40
    avatar = CAT_AVATAR_LEVEL_HAPPINESS_GT_30_OR_LT_60
    MIN_SATIETY = 0
    MAX_SATIETY = 100
    MIN_HAPPINESS = 0
    MAX_HAPPINESS = 100

    @classmethod
    def changing_avatar(cls):
        if cls.happiness >= 60:
            cls.avatar = CAT_AVATAR_LEVEL_HAPPINESS_GT_60
        elif cls.happiness < 60 and cls.happiness >= 30:
            cls.avatar = CAT_AVATAR_LEVEL_HAPPINESS_GT_30_OR_LT_60
        else:
            cls.avatar = CAT_AVATAR_LEVEL_HAPPINESS_LT_30

    @classmethod
    def play(cls):
        if not cls.is_sleeping:
            cls.happiness = min(cls.MAX_HAPPINESS, cls.happiness + 15)
            cls.satiety = max(cls.MIN_SATIETY, cls.satiety - 10)

            chance = random.randint(1, 3)
            if chance == 1:
                cls.happiness = cls.MIN_HAPPINESS
        else:
            cls.happiness = max(cls.MIN_HAPPINESS, cls.happiness - 5)

            cls.changing_avatar()


    @classmethod
    def feed(cls):
        if not cls.is_sleeping:
            cls.satiety = min(cls.MAX_SATIETY, cls.satiety + 15)
            cls.happiness = min(cls.MAX_HAPPINESS, cls.happiness + 5)
            if cls.satiety > cls.MAX_SATIETY:
                cls.happiness = max(cls.MIN_HAPPINESS, cls.happiness - 30)

            cls.changing_avatar()




            # def feed(cls):
            #     if not cls.is_sleeping:
            #         if cls.satiety < 100:
            #             cls.satiety += 15
            #             cls.happiness += 5
            #             if cls.satiety > 100:
            #                 cls.happiness -= 30
            #
            #         cls.changing_avatar()