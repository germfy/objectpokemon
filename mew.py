from basepokemon import BasePokemon, BaseMove, Type


class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(100)
        self.spend_attack(0)
        self.spend_defence(0)
        self.add_move(Lanzallamas())
        self.add_move(Burbujas())
        self.add_move(Terremoto())
        self.add_move(Patada())
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Mew"

    def choose_move(self, enemy):

        if enemy.type == Type.FIRE:
            return self.get_move_by_name("Burbujas")
        elif enemy.type == Type.WATER:
            return self.get_move_by_name("Terremoto")
        elif enemy.type == Type.EARTH:
            return self.get_move_by_name("Lanzallamas")
        else:
            return self.get_move_by_name("Patada")


class Lanzallamas(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Lanzallamas"


class Burbujas(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Burbujas"


class Terremoto(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Terremoto"


class Patada(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Patada"
