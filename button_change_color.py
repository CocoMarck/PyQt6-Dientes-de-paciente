from Modulos.Modulo_System import CleanScreen
from Modulos.color_diente import (
    get_data,
    get_id,
    get_all_id,
    
    get_id_name,
    get_id_dir,

    get_diente,
    
    get_pacientes,
    
    get_section_color,
    
    save_paciente,

    save_diente,

    set_id,
    
    remove_id,
)

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


# Probar metodos para los pacientes
list_paciente = get_pacientes()
if not list_paciente == None:
    for paciente in list_paciente:
        print(
            f'ID: {paciente[0]}\n'
            f'Name: {paciente[1]}\n'
            f'Remove: {paciente[2]}\n'
            f'Date: {paciente[3]}\n\n'
        )

#save_paciente(name='Una tercera persona')
#remove_id(id=2)
#set_id(id=2)

print(get_data())
print( get_id_name() )
print( get_id_dir() )
print( f'{type( get_id() )} {get_id()}' )
print( f'{type( get_all_id() )} {get_all_id()}' )

print(get_pacientes())
input()

# Probar get diente
print(get_diente())


class Window_Main(QWidget):
    def __init__(self, square=20, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('Change button color')
        self.resize(256, 256)
        
        # Contenedor principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Espacio entre botones
        space = int(square*1.1)
        
        # Seccion Vertical 1
        # Contenedor Horizontal - Dientes/Botones 1.8 - 1.1
        hbox = QHBoxLayout()
        hbox.setSpacing(space) # Espaciado entre lo contenido en el hbox
        vbox_main.addLayout(hbox)
        
        hbox.addStretch()
        
        number = 1.9
        for i in range(0, 8, 1):
            # Numero de diente
            number -= 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            # 1   2
            #   3
            # 4   5
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
        
        # Seccion Vertical 1
        # Contenedor Horizontal - Dientes/Botones 2.1 - 2.8
        number = 2.0
        for i in range(0, 8, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
        
        hbox.addStretch()

        # Seccion Vertical 2
        # Contenedor Horizontal - Dientes/Botones 5.5 - 5.1
        hbox = QHBoxLayout()
        hbox.setSpacing(space) # Espaciado entre lo contenido en el hbox
        vbox_main.addLayout(hbox)

        hbox.addStretch()
        
        number = 5.6
        for i in range(0, 5, 1):
            # Numero de diente
            number -= 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
            
        # Seccion Vertical 2
        # Contenedor Horizontal - Dientes/Botones 6.1 - 6.5
        number = 6.0
        for i in range(0, 5, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
        
        hbox.addStretch()
            
        # Seccion Vertical 3
        # Contenedor Horizontal - Dientes/Botones 8.5 - 8.1
        hbox = QHBoxLayout()
        hbox.setSpacing(space) # Espaciado entre lo contenido en el hbox
        vbox_main.addLayout(hbox)

        hbox.addStretch()
        
        number = 8.6
        for i in range(0, 5, 1):
            # Numero de diente
            number -= 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )

        # Seccion Vertical 3
        # Contenedor Horizontal - Dientes/Botones 7.1 - 7.5
        number = 7.0
        for i in range(0, 5, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
        
        hbox.addStretch()

        # Seccion Vertical 4
        # Contenedor Horizontal - Dientes/Botones 4.8 - 4.1
        hbox = QHBoxLayout()
        hbox.setSpacing(space) # Espaciado entre lo contenido en el hbox
        vbox_main.addLayout(hbox)
        
        hbox.addStretch()
        
        number = 4.9
        for i in range(0, 8, 1):
            # Numero de diente
            number -= 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            # 1   2
            #   3
            # 4   5
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
        
        # Seccion Vertical 4
        # Contenedor Horizontal - Dientes/Botones 3.1 - 3.8
        number = 3.0
        for i in range(0, 8, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            hbox.addLayout(
                self.diente_buttons(number=number, square=square)
            )
        
        # Mostrar todo
        self.show()
        
        hbox.addStretch()
    
    def diente_buttons(self, number=1.8, square=24):
        # Grid para posicionar botones
        # Numero de diente y Botones
        # Posicionados asi:
        # Numero
        # 1   2
        #   3
        # 4   5
        grid = QGridLayout()
        grid.setSpacing(0) # Espaciado entre botones

        # Numero de diente
        button = QPushButton(str(number))
        button.setFixedSize(square, square)
        grid.addWidget(button, 0, 0)

        # Boton 1
        button_color = QPushButton()

        color = get_section_color(diente=number, section=1)
        if not color == None:
            button_color.setStyleSheet(
                f'background-color: {color}' 
            )

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
        
        color = get_section_color(diente=number, section=2)
        if not color == None:
            button_color.setStyleSheet(
                f'background-color: {color}' 
            )

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

        color = get_section_color(diente=number, section=3)
        if not color == None:
            button_color.setStyleSheet(
                f'background-color: {color}' 
            )

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
        
        color = get_section_color(diente=number, section=4)
        if not color == None:
            button_color.setStyleSheet(
                f'background-color: {color}' 
            )

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

        color = get_section_color(diente=number, section=5)
        if not color == None:
            button_color.setStyleSheet(
                f'background-color: {color}' 
            )

        button_color.clicked.connect(
            partial(
                self.evt_change_color_good, button=button_color,
                number=number, number_square=5
            )
        )
        button_color.setFixedSize(square, square)
        grid.addWidget(button_color, 3, 3)
        
        return grid
    
            
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

        # Guardar diente
        save_diente(
            number=number,
            section=number_square,
            color=color
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())