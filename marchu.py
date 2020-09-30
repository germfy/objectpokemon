from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(25)
        self.spend_attack(40)
        self.spend_defence(35)
        self.add_move(Olita())
        self.add_move(Granizo())
        self.add_move(Lluvia_acida())
        self.add_move(Tsunami())
        
        self.set_type(Type.WATER)
        self.move = 0
        self.moves = ["Olita de mar ~~", "Granizo! ", "Lluvia acida!!", "Tsunami!!!"]

    def get_name(self):
        return "Marchu"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Olita(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Olita de mar ~~"

class Granizo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Granizo"

class Lluvia_acida(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Lluvia acida!!"

class Tsunami(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Tsunami!!!"


