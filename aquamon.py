from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        self.spend_hp(60)
        self.spend_attack(20)
        self.spend_defence(20)
        self.add_move(WaterPipe())
        self.set_type(Type.WATER)

    def get_name(self):
        return "Aquamon"
    
    def choose_move(self,enemy):
        return self.get_move_by_name("WaterPipe")

class WaterPipe(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "WaterPipe"