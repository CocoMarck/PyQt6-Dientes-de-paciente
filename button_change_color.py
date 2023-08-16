import sys
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton
)
from functools import partial


class Window_Main(QWidget):
    def __init__(self, square=16, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('Change button color')
        self.resize(256, 256)
        
        # Contenedor principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Contenedor Horizontal - Botones
        hbox = QHBoxLayout()
        hbox.setSpacing(24) # Espaciado entre lo contenido en el hbox
        vbox_main.addLayout(hbox)
        
        for i in range(0, 8, 1):
            # Grid para posicionar botones
            # Botones
            # Posicionados asi:
            # 1   2
            #   3
            # 4   5
            grid = QGridLayout()
            grid.setSpacing(0) # Ecpaciado entre botones
            hbox.addLayout(grid)

            # Boton 1
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(self.evt_change_color_good, button=button_color)
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 0, 0)

            # Boton 2
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(self.evt_change_color_good, button=button_color)
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 0, 3)

            # Boton 3
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(self.evt_change_color_good, button=button_color)
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 1, 2)

            # Boton 4
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(self.evt_change_color_good, button=button_color)
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 2, 0)

            # Boton 5
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(self.evt_change_color_good, button=button_color)
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 2, 3)
        
        # Mostrar todo
        self.show()
            
    def evt_change_color_good(self, button):
        # Detectar el color actual del boton y cambiarlo en base a eso.
        color = button.styleSheet()
        
        if color == "":
            button.setStyleSheet("background-color: red")
            #button.setText('Red')
        elif 'red' in color:
            button.setStyleSheet("background-color: green")
            #button.setText('Green')
        elif 'green' in color:
            button.setStyleSheet("background-color: blue")
            #button.setText('Blue')
        elif 'blue' in color:
            button.setStyleSheet("background-color: black")
            #button.setText('Black')
        elif 'black' in color:
            button.setStyleSheet("")
            #button.setText('No color')
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())