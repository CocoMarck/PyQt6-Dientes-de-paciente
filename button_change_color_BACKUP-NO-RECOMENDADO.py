from Modulos.Modulo_System import CleanScreen
import csv
import pandas as pd
import os

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

def get_dientes(diente='info_dientes/diente_1.8.csv'):
    with open(diente, 'r', newline='') as info_diente:
        text_diente = csv.reader(info_diente)
        list_diente = []
        for line in text_diente:
            print(
                f'{type( int(line[0]) )} {line[0]}\n'
                f'{type( line[1] )} {line[1]}\n'
            )
            list_diente.append( [ line[0], line[1] ] )
        return list_diente
get_dientes()


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

        #Guardar info
        diente_csv = f'info_dientes/diente_{number}.csv'
        with open(
            diente_csv,
            'a', newline=''
        ) as info_text:
            if os.path.isfile(diente_csv):
                with open(diente_csv, 'r+') as f:
                    text = f.read()
                    f.seek(0, 0)
                    f.write(
                        (
                            f'{number_square},{color}'
                        ).rstrip('\r\n') + '\n' + text
                    )
            else:
                writer_csv = csv.writer(info_text, delimiter=',')
                writer_csv.writerow(
                    [
                    str(number_square),
                    str(color)
                    ]
                )
        df = pd.read_csv(
            f'info_dientes/diente_{number}.csv',  sep=',', header=None
        )
        csv_final = df.drop_duplicates(0)
        csv_final.to_csv(
            f'info_dientes/diente_{number}.csv',
            sep=',',
            header=None, index=False
        )
        print(csv_final)
        
                    
        #Guardar info
        #with open(
        #    f'info_dientes/diente_{number}.txt',
        #    'a'
        #) as info_text:
        #    info_text.write(
        #        f'diente={number_square},{color}\n'
        #        '\n'
        #    )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())