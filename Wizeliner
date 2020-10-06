from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(50)
        self.spend_attack(30)
        self.spend_defence(20)
        self.add_move(Bad_connection())
        self.add_move(Wizecat())
        self.add_move(Spill_beer())
        self.add_move(Coffee_burn())
        self.set_type(Type.FIRE)
        self.move = 0
        self.moves = ['Bad connection', "Wizecat", "Spill Beer", "Coffee Burn"]


    def get_name(self):
        return "Wizeliner"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Bad_connection(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Bad connection"

class Wizecat(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Wizecat"


class Spill_beer(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Spill Beer"


class Coffee_burn(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Coffee Burn"
