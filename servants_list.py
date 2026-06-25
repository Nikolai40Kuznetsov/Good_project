import random as ran
ranks = ["-", "E-", "E", "E+", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "EX"]
# Создаем словарь для преобразования рангов в числовые значения
rank_to_value = {rank: i for i, rank in enumerate(ranks)}

class Servant():
    def __init__(self, name, strength, endurance, agility, mana, luck, np):
        self.name = name
        self.strength = self._convert_rank_to_value(strength)
        self.endurance = self._convert_rank_to_value(endurance)
        self.agility = self._convert_rank_to_value(agility)
        self.mana = self._convert_rank_to_value(mana)
        self.luck = self._convert_rank_to_value(luck)
        self.np = self._convert_rank_to_value(np)
        self.health = self.endurance * 250 + 1000

    def _convert_rank_to_value(self, rank):
        return rank_to_value.get(rank)
    
def summon():
    servant = ran.randint(1, 2)
    if servant == 1:
        return Servant("Артурия Пендрагон", "A", "A", "B", "B+", "C", "EX")
    if servant == 2:
        return Servant("NN", "E-", "E-", "E-", "E-", "E-", "E-")