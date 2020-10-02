from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(10)
        self.spend_attack(60)
        self.spend_defence(30)

        self.add_move(ataque_fuego())
        self.add_move(ataque_agua())
        self.add_move(ataque_tierra())
        self.add_move(ataque_normal())

        self.set_type(Type.WATER)

        self.move = 0
        self.moves = ['Ataque fuego', "Ataque agua", "Ataque tierra", "Ataque normal"]


    def get_name(self):
        return "pakomon"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class ataque_fuego(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(6)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Ataque fuego"

class ataque_agua(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(6)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Ataque agua"


class ataque_tierra(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(6)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Ataque tierra"


class ataque_normal(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(6)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Ataque normal"