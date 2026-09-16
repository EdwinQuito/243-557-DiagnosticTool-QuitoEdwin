class Sensor:
    """Représente un capteur du système."""

class Sensor:
    """Représente un capteur du système."""

    def __init__(
        self,
        name: str,
        unit: str,
        hardware,
    ) -> None:
        self.name = name
        self.unit = unit
        self.hardware = hardware

    def read(self) -> float:
        """Lit la valeur du capteur."""
        return self.hardware.read_sensor(self.name)