from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QGroupBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from src.models.Actuator import Actuator


class ActuatorWidget(QGroupBox):
    """Composant graphique représentant un actionneur."""

    def __init__(
        self,
        actuator: Actuator,
    ) -> None:
        super().__init__("Actionneur")

        self.actuator = actuator

        self.name_label = QLabel(
            self.actuator.name
        )

        self.state_label = QLabel()

        self.toggle_button = QPushButton()

        self.name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.state_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout = QVBoxLayout()

        layout.addWidget(self.name_label)
        layout.addWidget(self.state_label)
        layout.addWidget(self.toggle_button)

        self.setLayout(layout)

        self.toggle_button.clicked.connect(
            self.toggle_actuator
        )

        self.update_display()

    def toggle_actuator(self) -> None:
        """Inverse l'état de l'actionneur."""

        self.actuator.toggle()

        self.update_display()

    def update_display(self) -> None:
        """Actualise le texte et l'apparence."""

        if self.actuator.is_active:
            self.state_label.setText("ACTIF")
            self.toggle_button.setText("Désactiver")

            self.state_label.setStyleSheet(
                """
                font-size: 24px;
                font-weight: bold;
                padding: 12px;
                background-color: green;
                color: white;
                """
            )

        else:
            self.state_label.setText("INACTIF")
            self.toggle_button.setText("Activer")

            self.state_label.setStyleSheet(
                """
                font-size: 24px;
                font-weight: bold;
                padding: 12px;
                background-color: gray;
                color: white;
                """
            )