from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

from src.hardware.simulation_hardware import (
    SimulationHardware,
)

from src.models.Actuator import Actuator
from src.models.sensor import Sensor

from src.views.actuator_widget import ActuatorWidget
from src.views.Sensor_widget import SensorWidget


class MainWindow(QWidget):
    """Fenêtre principale du logiciel de diagnostic."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(
            "243-557 — DiagnosticTool"
        )

        self.resize(800, 450)

        self.title_label = QLabel(
            "Logiciel de diagnostic"
        )

        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title_label.setStyleSheet(
            """
            font-size: 28px;
            font-weight: bold;
            """
        )

        # Une seule instance représente
        # le matériel du système.
        self.hardware = SimulationHardware()

        # Création des modèles
        self.distance_sensor = Sensor(
            "Distance",
            "cm",
            self.hardware,
        )

        self.diagnostic_actuator = Actuator(
            "DEL de diagnostic",
            self.hardware,
        )

        # Création des composants graphiques
        self.distance_widget = SensorWidget(
            self.distance_sensor
        )

        self.actuator_widget = ActuatorWidget(
            self.diagnostic_actuator
        )

        # Layout horizontal des composants
        components_layout = QHBoxLayout()

        components_layout.addWidget(
            self.distance_widget
        )

        components_layout.addWidget(
            self.actuator_widget
        )

        components_layout.setSpacing(20)

        # Layout principal
        main_layout = QVBoxLayout()

        main_layout.addWidget(
            self.title_label
        )

        main_layout.addLayout(
            components_layout
        )

        main_layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        self.setLayout(main_layout)