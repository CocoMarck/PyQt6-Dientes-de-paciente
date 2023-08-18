from Modulos.Modulo_System import CleanScreen

import sys
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton
)
from PyQt6.QtCore import Qt
from functools import partial


class Window_Main(QWidget):
    def __init__(self, square=24, *args, **kwargs):
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
        
        number = 1.9
        for i in range(0, 8, 1):
            # Grid para posicionar botones
            # Numero de diente y Botones
            # Posicionados asi:
            # Numero
            # 1   2
            #   3
            # 4   5
            grid = QGridLayout()
            grid.setSpacing(0) # Ecpaciado entre botones
            hbox.addLayout(grid)
            
            # Numero de diente
            number -= 0.1
            number = round(number, 2)
            button = QPushButton(str(number))
            button.setFixedSize(square, square)
            grid.addWidget(button, 0, 0)
            #label = QLabel(str(round(number, 2)))
            #label.setAlignment(Qt.AlignmentFlag.AlignBottom)
            #grid.addWidget(label, 0, 0)

            # Boton 1
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(
                    self.evt_change_color_good, button=button_color,
                    number=number, number_square=1
                )
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 1, 0)

            # Boton 2
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(
                    self.evt_change_color_good, button=button_color,
                    number=number, number_square=2
                )
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 1, 3)

            # Boton 3
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(
                    self.evt_change_color_good, button=button_color,
                    number=number, number_square=3
                )
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 2, 2)

            # Boton 4
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(
                    self.evt_change_color_good, button=button_color,
                    number=number, number_square=4
                )
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 3, 0)

            # Boton 5
            button_color = QPushButton()
            button_color.clicked.connect(
                partial(
                    self.evt_change_color_good, button=button_color,
                    number=number, number_square=5
                )
            )
            button_color.setFixedSize(square, square)
            grid.addWidget(button_color, 3, 3)
        
        # Mostrar todo
        self.show()
            
    def evt_change_color_good(self, button, number, number_square):
        # Detectar el color actual del boton y cambiarlo en base a eso.
        color = button.styleSheet()
        
        if color == "":
            color = 'red'
        elif 'red' in color:
            color = 'green'
        elif 'green' in color:
            color = 'blue'
        elif 'blue' in color:
            color = 'black'
        elif 'black' in color:
            color = ''
        else:
            pass
        
        # Cambiar el color de boton
        if not color == "":
            button.setStyleSheet(f"background-color: {color}")
        else:
            color = None
            button.setStyleSheet("")
        
        # Imprimir el color actual del boton, el numero al que pertenece el boton, y el numero del boton.
        CleanScreen()
        info = (
            f'color: {color}\n'
            f'number: {number}\n'
            f'number_square: {number_square}'
        )
        print(info)
        
        # Guardar info
        #with open(
        #    f'info_dientes/diente_{number}_{number_square}.txt',
        #    'w'
        #) as info_text:
        #    info_text.write(info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())