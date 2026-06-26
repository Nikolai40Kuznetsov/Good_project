import random as ran
ranks = ["-", "E-", "E", "E+", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "A++", "EX"]
rank_to_value = {rank: i-1 for i, rank in enumerate(ranks)}

class Servant():
    def __init__(self, name, strength, endurance, agility, mana, luck, np, class_skill_1, class_skill_1_rank, class_skill_2, class_skill_2_rank):
        self.name = name
        self.strength = self.convert_rank_to_value(strength)
        self.endurance = self.convert_rank_to_value(endurance)
        self.agility = self.convert_rank_to_value(agility)
        self.mana = self.convert_rank_to_value(mana)
        self.luck = self.convert_rank_to_value(luck)
        self.np = self.convert_rank_to_value(np)
        self.class_skill_1 = class_skill_1
        self.class_skill_1_rank = self.convert_rank_to_value(class_skill_1_rank)
        self.class_skill_2 = class_skill_2
        self.class_skill_2_rank = self.convert_rank_to_value(class_skill_2_rank)
        self.health = self.endurance * 250 + 1000
        self.damage = self.strength * 25 + 100
        self.magical_resistance = self.mag_res()
        print(self.magical_resistance)
        self.mana_consumption = 20 * (1 - self.mana_cons() / 100)
        print(self.mana_consumption)

    def convert_rank_to_value(self, rank):
        return rank_to_value.get(rank)
    
    def mag_res(self):
        if self.class_skill_1 == "Сопротивление магии":
            persent = self.class_skill_1_rank * 6.25
            return persent 
        if self.class_skill_2 == "Сопротивление магии":
            persent = self.class_skill_2_rank * 6.25
            return persent
        else:
            return 0
    def mana_cons(self):
        if self.class_skill_1 == "Независимое действие":
            persent = self.class_skill_1_rank * 6.25
            return persent
        if self.class_skill_2 == "Независимое действие":
            persent = self.class_skill_2_rank * 6.25
            return persent
        else:
            return 0

def summon():
    servant = ran.randint(1, 3)
    if servant == 1:
        return Servant("Артурия Пендрагон", "A", "B", "B", "A", "A+", "A++", "Сопротивление магии", "A", "Верховая езда", "B")
    if servant == 2:
        return Servant("Гильгамеш", "B", "B", "B", "A", "A", "EX", "Сопротивление магии", "C", "Независимое действие", "A")
    if servant == 3:
        return Servant("NN", "E-", "E-", "E-", "E-", "E-", "E-", " ", " ", " ", "")