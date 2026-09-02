class Actuator:
    def __init__(self, name: str) -> None:
        self.name = name                              ## garder le nom
        self.active = False                           ## démarre inactive 

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def toggle(self) -> None:                          ##inversion
        self.active = not self.active