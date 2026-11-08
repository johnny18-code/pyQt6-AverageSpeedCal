import time
from turtle import distance
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QComboBox

import sys


class AveSpeedCalculator(QWidget):
    def __init__(self) -> None:
        super().__init__()  # Instantiate Mother
        self.setWindowTitle("Average Speed Calculator")

        # create Class for the the Grid
        grid = QGridLayout()

        # Set Widgets
        # 1 row
        distance = QLabel("Distance: ")
        self.input_distance = QLineEdit("")

        # instantiate the combo box
        self.comboBox = QComboBox()
        self.comboBox.addItems(
            ["Metric (KM)", "Imperial (Miles)"])  # add the Items
        self.comboBox.currentTextChanged.connect(self.text_changed)
        self.output_label_comboBox = ""

        # 2nd row
        time = QLabel("Time (hours): ")
        self.input_time = QLineEdit("")

        # 3rd row - Button triggers
        button = QPushButton("Calculate Average Speed")
        button.clicked.connect(self.calculateSpeed)

        # 4th row output
        self.output_label = QLabel("")

        # Plot the Widgets
        grid.addWidget(distance, 0, 0)
        grid.addWidget(self.input_distance, 0, 1)
        grid.addWidget(self.comboBox, 0, 2)

        grid.addWidget(time, 1, 0)
        grid.addWidget(self.input_time, 1, 1)

        grid.addWidget(button, 2, 0)

        grid.addWidget(self.output_label, 3, 0)

        # set the Grid
        self.setLayout(grid)

    def calculateSpeed(self):
        calc_input_disntance = float(self.input_distance.text())
        calc_input_time_hours = float(self.input_time.text())
        # Chosen Box
        # print(self.output_label_comboBox)
        # # Basic Formula for KM
        # if self.output_label_comboBox == "Metric (KM)":
        #     averagespeed = int(calc_input_disntance) / \
        #         int(calc_input_time_hours)
        #     self.output_label.setText(
        #         f"{averagespeed} is  your Average Speed in KM per Hour ")
        # elif self.output_label_comboBox == "Imperial (Miles)":
        #     averagespeed = int(calc_input_disntance) / \
        #         int(calc_input_time_hours)
        #     self.output_label.setText(
        #         f"{averagespeed} is  your Average Speed in Miles Per Hour ")
        # else:
        #     self.output_label.setText("")

        # Calculate Average Speed
        speed = calc_input_disntance / calc_input_time_hours
        unit = ""
        # get current selected from the combo box with the currentText
        if self.comboBox.currentText() == "Metric (KM)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.comboBox.currentText() == "Imperial (Miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        # display result
        self.output_label.setText(f"Average Speed ,{speed} {unit}")

    def text_changed(self, s):
        self.output_label_comboBox = s


app = QApplication(sys.argv)  # sys.argv allows command line arguments?
window = AveSpeedCalculator()
window.show()
sys.exit(app.exec())


if __name__ == "__main__":
    print("Average Speed Calculator ")
