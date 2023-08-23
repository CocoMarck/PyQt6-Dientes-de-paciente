from Modulos.Modulo_System import (
    get_system,
    CleanScreen
)
from Modulos.Modulo_Language import get_text as Lang
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
    QDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox
)
from PyQt6.QtCore import Qt
from functools import partial


# Probar metodos para los pacientes
#list_paciente = get_pacientes()
#if not list_paciente == None:
#    for paciente in list_paciente:
#        print(
#            f'ID: {paciente[0]}\n'
#            f'Name: {paciente[1]}\n'
#            f'Remove: {paciente[2]}\n'
#            f'Date: {paciente[3]}\n\n'
#        )

#save_paciente(name='Una tercera persona')
#remove_id(id=2)
#set_id(id=2)

#print(get_data())
#print( get_id_name() )
#print( get_id_dir() )
#print( f'{type( get_id() )} {get_id()}' )
#print( f'{type( get_all_id() )} {get_all_id()}' )

#print(get_pacientes())
#input()

# Probar get diente
#print(get_diente())


class Window_Main(QWidget):
    def __init__(self, square=20, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle( Lang('paciente_teeth') )
        self.resize(256, 256)
        
        # Contenedor principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Seccion Vertical 0
        # Boton para guardar y borrar, y seleccionar paciente
        # Contenedor Horizontal
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        button_set_paciente = QPushButton(Lang('select'))
        button_set_paciente.clicked.connect(self.evt_set_paciente)
        hbox.addWidget(button_set_paciente)
        
        hbox.addStretch()
        
        self.combobox_paciente = QComboBox()
        dict_paciente = self.dict_paciente()
        for paciente in dict_paciente.keys():
            self.combobox_paciente.addItem( paciente )

            current_paciente = get_id_name()
            if not current_paciente == None:
                current_paciente = self.combobox_paciente.findText(
                    current_paciente
                )
                self.combobox_paciente.setCurrentIndex(current_paciente)
                

        hbox.addWidget(self.combobox_paciente)
        
        hbox.addStretch()
        
        vbox = QVBoxLayout()
        hbox.addLayout(vbox)

        button_new_paciente = QPushButton(Lang('new'))
        button_new_paciente.clicked.connect(self.evt_new_paciente)
        vbox.addWidget(button_new_paciente)
        
        button_remove_paciente = QPushButton(Lang('remove'))
        button_remove_paciente.clicked.connect(self.evt_remove_paciente)
        vbox.addWidget(button_remove_paciente)
        
        # Espaciando, para separar botones de dientes, de botones de sleccion de paciente
        vbox_main.addStretch()
        
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
            
        hbox.addStretch()
        
        # Espaciando, para separar botones de dientes, de botones de sleccion de paciente
        vbox_main.addStretch()
        
        # Mostrar todo
        self.show()
    
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
    
    def dict_paciente(self):
        dict_paciente = {}
    
        list_paciente = get_pacientes()
        if not list_paciente == None:
            for paciente in list_paciente:
                if paciente[2] == 0:
                    dict_paciente.update( {paciente[1] : paciente[0]} )
            return dict_paciente
    
    def evt_set_paciente(self):
        dict_paciente = self.dict_paciente()
        
        paciente = self.combobox_paciente.currentText()
        if paciente in dict_paciente:
            set_id( id=dict_paciente[paciente] )
            # Cerrar y volver abrir el programa
            warning_exit(self)
            self.close()
        else:
            pass
    
    def evt_new_paciente(self):
        Dialog_new_paciente(self).exec()
    
    def evt_remove_paciente(self):
        # Dar de baja un paciente
        paciente = self.combobox_paciente.currentText()

        # Pregunta si quiere borrar o no.
        message_quest = QMessageBox.question(
            self,
            Lang('remove'),

            f'{Lang("quest_remove_paciente")}:\n'
            f'"{paciente}"',
            
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        
        if message_quest == QMessageBox.StandardButton.Yes:
            # Dar de baja el Paciente actual en el Combo Box
            dict_paciente = self.dict_paciente()
            if not dict_paciente == None:
                remove_id( dict_paciente[paciente] )
                warning_exit(self)
                self.close()
        else:
            pass
            
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


def warning_exit(parent=None):
    import threading

    # Mensaje de advertencia, ¡que se cerrara el programa!
    QMessageBox.warning(
        parent,
        Lang('warning'),

        Lang('for_now_close_app') + '\n' +
        Lang('you_need_open_app')
    )

    # Hilo/Subproceso para volver a abrir esta app
    thread = threading.Thread(
        target=reboot_app
    )
    thread.start()
    
    # Salir
    app.exit()


def reboot_app():
    # Reiniciar app
    import subprocess
    
    system = get_system()
    if system == 'linux':
        #subprocess.run(['./Dientos'])
        subprocess.run(['python3', 'Dientos.py'])
    elif system == 'win':
        #subprocess.run(['start', '.\\Dientos.exe'])
        subprocess.run(['python', 'Dientos.py'])


class Dialog_new_paciente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(Lang('add_paciente'))
        self.resize(256, -1)
        
        # Contenedor principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Secciones verticales - Entry de paciente y button para crear paciente
        self.entry_paciente = QLineEdit(
            self,
            placeholderText=Lang('paciente')
        )
        vbox_main.addWidget(self.entry_paciente)
        
        vbox_main.addStretch()
        
        button_new_paciente = QPushButton( Lang('add') )
        button_new_paciente.clicked.connect(self.evt_new_paciente)
        vbox_main.addWidget(button_new_paciente)
    
    def evt_new_paciente(self):
        paciente = self.entry_paciente.text()
        if paciente == '':
            pass
        else:
            save_paciente(paciente)

            # Se supone que se tiene que reiniciar la app - Y solo se cierra
            warning_exit(self)
            app.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())