from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        self.spend_hp(25)
        self.spend_attack(35)
        self.spend_defence(40)
        self.add_move(Powerful_Nucleus())
        self.add_move(Ash())
        self.add_move(Magic_Wave())
        self.add_move(Shell())
        self.move = 0
        self.moves = ["Powerful_Nucleus","Ash","Magic_Wave","Shell"]
        self.set_type(Type.WATER)

    def get_name(self):
        return "Squirtle"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Powerful_Nucleus(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.EARTH)


    def get_name(self):
        return "Powerful_Nucleus"

class Ash(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.FIRE)


    def get_name(self):
        return "Ash"
        
class Magic_Wave(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.WATER)


    def get_name(self):
        return "Magic_Wave"
        
class Shell(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.NORMAL)


    def get_name(self):
        return "Shell"
