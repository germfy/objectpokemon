from basepokemon import BasePokemon, BaseMove, Type


class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(50)
        self.spend_attack(50)
        self.spend_defence(0)
        self.add_move(Echatelo())
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Chocolob"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)


class Echatelo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "le avento tierra"


class Cachetada(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "le dijo criada"
