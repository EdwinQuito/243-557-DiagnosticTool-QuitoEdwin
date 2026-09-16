from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGroupBox, 
)
from src.models.sensor import Sensor 
from src.models.Actuator import Actuator 
from src.hardware.simulation_hardware import SimulationHardware

class MainWindow(QWidget):
    """Fenêtre principale du logiciel de diagnostic."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("243-557 — DiagnosticTool")
        self.hardware = SimulationHardware()
        self.resize(360, 220)

        self.sensor = Sensor(
            "Distance",
            "cm",
            self.hardware,
        )

        self.actuator = Actuator("LED de diagnostic")
        self.title_label = QLabel("Logiciel de diagnostic - Edwin Quito")
        self.sensor_name_label = QLabel(f"Capteur : {self.sensor.name}")
        self.sensor_value_label = QLabel("Valeur : ---")
        self.read_button = QPushButton("Lire le capteur")
        self.actuator_name_label = QLabel(f"Actionneur : {self.actuator.name}")
        self.actuator_state_label = QLabel("État : Inactif")
        self.actuator_button = QPushButton("Changer l'état")

        sensor_group = QGroupBox("Capteur")
        sensor_layout = QVBoxLayout()
        sensor_layout.addWidget(self.sensor_name_label)
        sensor_layout.addWidget(self.sensor_value_label)
        sensor_layout.addWidget(self.read_button)

        sensor_group.setLayout(sensor_layout)

        actuator_group = QGroupBox("Actionneur")

        actuator_layout = QVBoxLayout()
        actuator_layout.addWidget(self.actuator_name_label)
        actuator_layout.addWidget(self.actuator_state_label)
        actuator_layout.addWidget(self.actuator_button)

        actuator_group.setLayout(actuator_layout) 
        

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(sensor_group)
        layout.addWidget(actuator_group)

        self.setLayout(layout)

        self.read_button.clicked.connect(self.read_sensor)
        self.actuator_button.clicked.connect(self.toggle_actuator)

    def read_sensor(self) -> None:
        """Simule la lecture d'un capteur de température."""
        value = self.sensor.read()

        self.sensor_value_label.setText(
            f"Valeur : {value} {self.sensor.unit}")

    def toggle_actuator(self) -> None:
    ##Change l'état de l'actionneur.##
        self.actuator.toggle()

        if self.actuator.active:
            self.actuator_state_label.setText("État : Actif")
        else:
              self.actuator_state_label.setText("État : Inactif")       