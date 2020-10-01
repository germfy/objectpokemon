from basepokemon import BasePokemon, BaseMove, Type
#from random import seed
#from random import randint
#seed(1)
#self.move = randint(0,4)

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        self.spend_hp(60)
        self.spend_attack(20)
        self.spend_defence(20)
        self.add_move(WaterPipe())
        self.add_move(FireBall())
        self.add_move(EarthQuake())
        self.add_move(Sandbox())
        self.move = 0
        self.moves = ["WaterPipe","FireBall","EarthQuake","Sandbox"]

        # self.set_type(Type.WATER)

    def get_name(self):
        return "Aquamon"
    
    def choose_move(self,enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class WaterPipe(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "WaterPipe"

class FireBall(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "FireBall"

class EarthQuake(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)
    
    def get_name(self):
        return "EarthQuake"

class Sandbox(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Sandbox"