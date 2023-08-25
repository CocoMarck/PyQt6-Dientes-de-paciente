from Modulos.Modulo_System import (
    get_system,
    CleanScreen
)
from Modulos.Modulo_Language import get_text as Lang
from Modulos.color_diente import (
    get_id,
    get_id_name,

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
    QInputDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox
)
from PyQt6.QtGui import QIcon
from functools import partial


class Window_Main(QWidget):
    def __init__(self, square=20, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle( Lang('paciente_teeth') )
        #self.resize(256, 256)
        
        # Contenedor principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Seccion Vertical 0
        # Boton para guardar y borrar, y combobox para seleccionar paciente
        # Contenedor Horizontal
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        button_new_paciente = QPushButton(Lang('new'))
        button_new_paciente.clicked.connect(self.evt_new_paciente)
        hbox.addWidget(button_new_paciente)
        
        hbox.addStretch()
        
        self.combobox_paciente = QComboBox()
        dict_paciente = self.dict_paciente()
        self.update_combobox()
        self.combobox_paciente.activated.connect(self.evt_set_paciente)
        self.combobox_paciente.setFixedSize(512, 24)
        hbox.addWidget(self.combobox_paciente)
        #hbox.setStretchFactor(self.combobox_paciente, 1)
        
        hbox.addStretch()
        
        button_remove_paciente = QPushButton(Lang('remove'))
        button_remove_paciente.clicked.connect(self.evt_remove_paciente)
        hbox.addWidget(button_remove_paciente)
        
        # Espaciando, para separar botones de dientes, de botones de sleccion de paciente
        vbox_main.addStretch()
        
        # Espacio entre botones
        space = int(square/2)
        
        # Diccionario que guardara los dientes: y sus colores.
        self.dict_diente = {
            #numero de diente: lista de botones.
        }

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
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
            )
            
        # Cruz - Linea Horizontal 1
        label = QLabel()
        label.setStyleSheet('QLabel{background-color:black}')
        hbox.addWidget(label)
        
        # Seccion Vertical 1
        # Contenedor Horizontal - Dientes/Botones 2.1 - 2.8
        number = 2.0
        for i in range(0, 8, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
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
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
            )
            
        # Cruz - Linea Horizontal 2
        label = QLabel()
        label.setStyleSheet('QLabel{background-color:black}')
        hbox.addWidget(label)
            
        # Seccion Vertical 2
        # Contenedor Horizontal - Dientes/Botones 6.1 - 6.5
        number = 6.0
        for i in range(0, 5, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
            )
        
        hbox.addStretch()
        
        # Cruz Linea Vertical
        label = QLabel()
        label.setStyleSheet('QLabel{background-color:black}')
        #label.setFixedSize(
        #    ( (square*48) + ( (space)*16 ) ), 8
        #)
        vbox_main.addWidget(label)
            
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
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
            )
        
        # Cruz - Linea Horizontal 3
        label = QLabel()
        label.setStyleSheet('QLabel{background-color:black}')
        hbox.addWidget(label)

        # Seccion Vertical 3
        # Contenedor Horizontal - Dientes/Botones 7.1 - 7.5
        number = 7.0
        for i in range(0, 5, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
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
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
            )
            
        # Cruz - Linea Horizontal 4
        label = QLabel()
        label.setStyleSheet('QLabel{background-color:black}')
        hbox.addWidget(label)
        
        # Seccion Vertical 4
        # Contenedor Horizontal - Dientes/Botones 3.1 - 3.8
        number = 3.0
        for i in range(0, 8, 1):
            # Numero de diente
            number += 0.1
            number = round(number, 2)

            # Establecer el Diente y sus botones
            self.diente=(
                self.diente_buttons(number=number, square=square)
            )
            self.dict_diente.update(
                {
                    number :
                    [ self.diente[1], self.diente[2],
                    self.diente[3], self.diente[4],
                    self.diente[5] ]
                }
            )
            hbox.addLayout(
                self.diente[0]
            )
            
        hbox.addStretch()
        
        # Espaciando, para separar botones de dientes, de botones de sleccion de paciente
        vbox_main.addStretch()
        
        # Obtener los colores de cada diente
        self.get_diente_colors()
        
        # Mostrar todo
        self.showMaximized()
        #self.show()
    
    def diente_buttons(self, number=1.8, square=24):
        # Grid para posicionar botones
        # Numero de diente y Botones
        # Posicionados asi:
        # Numero
        # 1 1 1
        # 2 3 4
        # 5 5 5
        # Numero "1" estirado de "2 a 4" (no tres 1)
        # Numero "3" estirado de "2 a 4" (no tres 5)
        grid = QGridLayout()
        grid.setSpacing(0) # Espaciado entre botones

        # Numero de diente
        button = QPushButton(str(number))
        button.setFixedSize(square, square)
        grid.addWidget(button, 0, 0)

        # Boton 1
        button_1 = QPushButton()
        button_1.clicked.connect(
            partial(
                self.evt_change_color, button=button_1,
                number=number, number_square=1
            )
        )
        button_1.setFixedSize(square*3, square)
        grid.addWidget(button_1, 1, 0, 1, 3)

        # Boton 2
        button_2 = QPushButton()
        button_2.clicked.connect(
            partial(
                self.evt_change_color, button=button_2,
                number=number, number_square=2
            )
        )
        button_2.setFixedSize(square, square)
        grid.addWidget(button_2, 2, 0)

        # Boton 3
        button_3 = QPushButton()
        button_3.clicked.connect(
            partial(
                self.evt_change_color, button=button_3,
                number=number, number_square=3
            )
        )
        button_3.setFixedSize(square, square)
        grid.addWidget(button_3, 2, 1)

        # Boton 4
        button_4 = QPushButton()
        button_4.clicked.connect(
            partial(
                self.evt_change_color, button=button_4,
                number=number, number_square=4
            )
        )
        button_4.setFixedSize(square, square)
        grid.addWidget(button_4, 2, 2)

        # Boton 5
        button_5 = QPushButton()
        button_5.clicked.connect(
            partial(
                self.evt_change_color, button=button_5,
                number=number, number_square=5
            )
        )
        button_5.setFixedSize(square*3, square)
        grid.addWidget(button_5, 3, 0, 3, 3)
        
        return [grid, button_1, button_2, button_3, button_4, button_5]

    def get_diente_colors(self):
        # Obener los colore de cada diente disponible
        for key in self.dict_diente.keys():
            number = key
            diente = self.dict_diente[key]

            button_1 = diente[0]
            button_2 = diente[1]
            button_3 = diente[2]
            button_4 = diente[3]
            button_5 = diente[4]
            
            color = get_section_color(diente=number, section=1)
            if not color == None:
                button_1.setStyleSheet(
                    f'background-color: {color}' 
                )

            color = get_section_color(diente=number, section=2)
            if not color == None:
                button_2.setStyleSheet(
                    f'background-color: {color}' 
                )

            color = get_section_color(diente=number, section=3)
            if not color == None:
                button_3.setStyleSheet(
                    f'background-color: {color}' 
                )

            color = get_section_color(diente=number, section=4)
            if not color == None:
                button_4.setStyleSheet(
                    f'background-color: {color}' 
                )

            color = get_section_color(diente=number, section=5)
            if not color == None:
                button_5.setStyleSheet(
                    f'background-color: {color}' 
                )

    def clear_diente_colors(self):
        # Limpiar los colores de todos los dientes.
        for key in self.dict_diente.keys():
            number = key
            diente = self.dict_diente[key]

            button_1 = diente[0]
            button_2 = diente[1]
            button_3 = diente[2]
            button_4 = diente[3]
            button_5 = diente[4]
            
            button_1.setStyleSheet('')
            button_2.setStyleSheet('')
            button_3.setStyleSheet('')
            button_4.setStyleSheet('')
            button_5.setStyleSheet('')
    
    def update_diente_colors(self):
        self.clear_diente_colors()
        self.get_diente_colors()
    
    def dict_paciente(self):
        dict_paciente = {}
    
        list_paciente = get_pacientes()
        if not list_paciente == None:
            for paciente in list_paciente:
                if paciente[2] == 0:
                    dict_paciente.update( 
                        {f'{paciente[0]}. {paciente[1]}' : paciente[0]} 
                    )
            return dict_paciente
    
    def update_combobox(self):
        # Limpiar combobox, y agregar pacientes al combobox.
        # Asi: numero_id. nombre_paciente
        self.combobox_paciente.clear()
        dict_paciente = self.dict_paciente()
        for paciente in dict_paciente.keys():
            self.combobox_paciente.addItem( paciente )

            current_paciente = get_id_name()
            if not current_paciente == None:
                current_paciente = self.combobox_paciente.findText(
                    f'{get_id()}. {current_paciente}'
                )
                self.combobox_paciente.setCurrentIndex(current_paciente)
    
    def evt_set_paciente(self):
        # Seleccionar un paciente
        dict_paciente = self.dict_paciente()
        
        paciente = self.combobox_paciente.currentText()
        if paciente in dict_paciente:
            id = dict_paciente[paciente]
            set_id( id=id )

            self.update_diente_colors()
            #warning_exit(self)
            #self.close()
        else:
            pass
    
    def evt_new_paciente(self):
        # Crear un nuevo paciente
        new_paciente, ok = QInputDialog.getText(
            self,
            Lang('new'),
            
            Lang('add_paciente')
        )
        if ok and new_paciente:
            if new_paciente == '':
                pass
            else:
                save_paciente(new_paciente)
                self.update_diente_colors()
                self.update_combobox()
                #warning_exit(self)
                #self.close()
        else:
            pass
    
    def evt_remove_paciente(self):
        # Dar de baja un paciente
        paciente = self.combobox_paciente.currentText()

        if not paciente == '':
            # Pregunta si quiere borrar el paciente o no.
            message_quest = QMessageBox.question(
                self,
                Lang('remove'),

                f'{Lang("quest_remove_paciente")}:\n'
                f'"{paciente}"',
                
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No
            )
            
            if (
                message_quest == QMessageBox.StandardButton.Yes
            ):
                # Dar de baja el Paciente actual en el Combo Box
                dict_paciente = self.dict_paciente()
                if not dict_paciente == None:
                    remove_id( dict_paciente[paciente] )
                    self.update_diente_colors()
                    self.update_combobox()
                    #warning_exit(self)
                    #self.close()
            else:
                pass
        else:
            pass
            
    def evt_change_color(self, button, number, number_square):
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


def warning_exit(parent=None, thread=True):
    import threading
    # Mensaje de advertencia, ¡que se cerrara el programa!
    QMessageBox.warning(
        parent,
        Lang('warning'),

        Lang('for_now_close_app') + '\n' +
        Lang('you_need_open_app')
    )

    # Hilo/Subproceso para volver a abrir esta app
    if thread == True:
        thread = threading.Thread(
            target=reboot_app
        )
        thread.start()
    else:
        pass
    
    # Salir
    app.exit()


def reboot_app():
    # Reiniciar app
    import subprocess
    
    system = get_system()
    app_exec = 'Dientos'
    if system == 'linux':
        #subprocess.run([f'./{app_exec}'])
        subprocess.run(['python3', f'{app_exec}.py'])
    elif system == 'win':
        #subprocess.run(['start', f'{app_exec}.exe'])
        subprocess.run(['python', f'{app_exec}.py'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())