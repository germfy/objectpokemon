from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        self.spend_hp(50)
        self.spend_attack(20)
        self.spend_defence(30)

        # List of movements
        self.add_move(Megahorn())
        self.add_move(CloseCombat())
        self.add_move(FuryAttack())

        self.move = 0
        self.moves = ['Megahorn', "Close Combat", "Fury Attack"]
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Heracross"
    
    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

    
class Megahorn(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Megahorn"

class CloseCombat(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Close Combat"

class FuryAttack(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Fury Attack"