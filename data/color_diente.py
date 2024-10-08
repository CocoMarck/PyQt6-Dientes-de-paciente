#from Modulos.Modulo_Files import(
#    Files_List
#)
from logic.Modulo_Text import(
    Text_Read,
    Ignore_Comment,
    Text_Separe
)

import csv
import pandas as pd
import os, sys




# Dirección de dientes
current_dir = os.path.dirname( os.path.abspath(sys.argv[0]) )
dir_data = os.path.join(current_dir, 'resources')

dir_dientes= os.path.join( dir_data, 'info_dientes')




# Otros
def get_data(mode_dict=True):
    '''Obtener datos de cantidad de ids, el id actual y su nombre'''    
    id_dientes_file = f'{dir_dientes}/id_dientes.dat'
    if os.path.isfile(id_dientes_file):
        # Leer texto y ignorar comentarios tipo '#'
        id_dientes_archive = Text_Read(
            id_dientes_file,
            'ModeText'
        )
        id_dientes_data = Ignore_Comment(
            text=id_dientes_archive,
            comment='#'
        )
        # Agregar valores en el texto a un diccionario
        id_dientes_data = Text_Separe(
            text=id_dientes_data,
            text_separe='='
        )
        
        # Retornar en modo solo los datos en modo diccionario
        # O retornar el texto completo
        if mode_dict == True:
            # Retornar en modo diccionario
            return id_dientes_data
        else:
            # Retornar en modo texto
            return id_dientes_archive
    else:
        all_pacientes = 0
        for paciente in get_pacientes():
            all_pacientes += 1

        with open(id_dientes_file, 'w') as id_dientes:
            id_dientes.write(
                f'all_id={all_pacientes}\n'
                'current_id=\n'
                'current_id_name='
            )

        # Leer texto
        id_dientes_data = Text_Read(
            id_dientes_file,
            'ModeText'
        )
        # Agregar valores en el texto a un diccionario
        id_dientes_data = Text_Separe(
            text=id_dientes_data,
            text_separe='='
        )
        
        # Retornar en modo solo los datos en modo diccionario
        # O retornar el texto completo
        if mode_dict == True:
            # Retornar en modo diccionario
            return id_dientes_data
        else:
            # Retornar en modo texto
            return id_dientes_archive


def get_id():
    '''Obtener el id actual'''
    data = get_data()
    
    current_id = data['current_id']
    if current_id == '':
        return 0
    else:
        return int(current_id)


def get_id_name():
    '''Obtener el nombre del id actual'''
    data = get_data()
    
    current_id_name = data['current_id_name']
    if current_id_name == '':
        return 'Default'
    else:
        return current_id_name


def get_all_id():
    '''Obtener el numero de ids'''
    data = get_data()
    
    all_id = data['all_id']
    if all_id == '':
        return 0
    else:
        return int(all_id)


def get_id_dir():
    '''Obtener el directorio del id actual'''
    data = get_data()
    
    current_id = data["current_id"]
    if current_id == '':
        return f'{dir_dientes}/Default'
    else:
        return f'{dir_dientes}/{current_id}'


def get_pacientes():
    paciente_csv = f'{dir_dientes}/paciente.csv'
    if os.path.isfile(paciente_csv):
        with open(paciente_csv, 'r') as paciente:
            text_paciente = csv.reader(paciente)
            list_paciente = []
            for line in text_paciente:
                list_paciente.append( 
                    [ int(line[0]), line[1], int(line[2]), line[3] ]
                )

        return list_paciente
    else:
        pass


def save_paciente(name=None):
    '''Guardar un paciente, se guarda un id y su nombre establecido por el parametro "name", la fecha en que se guardo y se establece en el archivo "id_dientes.dat"'''
    if type(name) is str:
        pass
    else:
        name = 'Default'

    # Verificar que el id sea otro nombre, y establecerlo si lo es o no con una variable tipo bool
    paciente_csv = f'{dir_dientes}/paciente.csv'
    same_name = False
    if os.path.isfile(paciente_csv):
        with open(paciente_csv, 'r') as paciente:
            text_paciente = csv.reader(paciente)
            list_paciente = []
            for line in text_paciente:
                list_paciente.append( 
                    str(line[1])
                )
        for paciente in list_paciente:
            if paciente == name:
                #same_name = True ;Desactivar esta funcion, ya que no es tan necesaria.
                same_name = False
            else:
                same_name = False
    else:
        pass

    # Guardar ID, solo si el no es el mismo nombre de un id ya existente
    if not same_name == True:
        all_id = get_all_id()
        current_id = all_id + 1
        
        os.mkdir(f'{dir_dientes}/{current_id}')

        with open(
            f'{dir_dientes}/paciente.csv',
            'a', newline=''
        ) as paciente_csv:
            writer_csv = csv.writer(paciente_csv, delimiter=',')
            writer_csv.writerow(
                [
                int(current_id),
                str(name),
                int(0),
                '0000-00-00'
                ]
            )
        
        # Establecer el id creado en "id_dientes.dat"
        id_dientes_archive = get_data(mode_dict=False)
        text_ready = ''
        for line in id_dientes_archive.split('\n'):
            if line.startswith('all_id='):
                line = f'all_id={current_id}'
            elif line.startswith('current_id='):
                line = f'current_id={current_id}'
            elif line.startswith('current_id_name='):
                line = f'current_id_name={name}'
            else:
                pass
            text_ready += line + '\n'
        
        with open(f'{dir_dientes}/id_dientes.dat', 'w') as id_dientes:
            id_dientes.write( text_ready[:-1] )
    else:
        pass


def set_id(id=0):
    '''Establecer un id en espcifico'''
    all_id = get_all_id()
    if (
        not all_id == 0 and
        not id <= 0
    ):
        if id <= all_id:
            paciente_csv = f'{dir_dientes}/paciente.csv'
            if os.path.isfile(paciente_csv):
                with open(paciente_csv, 'r') as paciente:
                    text_paciente = csv.reader(paciente)
                    list_paciente = []
                    for line in text_paciente:
                        list_paciente.append( 
                            [ int(line[0]), line[1], line[2], line[3] ]
                        )

                # Establecer parametros para agregarlos al "id_dientes.dat"
                current_id = id
                name = ''
                remove = 0
                for paciente in list_paciente:
                    if paciente[0] == id:
                        name = paciente[1]
                        remove = int(paciente[2])
                    else: 
                        pass

                if remove == 1:
                    current_id = ''
                    name = ''
                else:
                    pass

                # Establecer el id creado en "id_dientes.dat"
                id_dientes_archive = get_data(mode_dict=False)
                text_ready = ''
                for line in id_dientes_archive.split('\n'):
                    if line.startswith('current_id='):
                        line = f'current_id={current_id}'
                    elif line.startswith('current_id_name='):
                        line = f'current_id_name={name}'
                    else:
                        pass
                    text_ready += line + '\n'
                
                with open(f'{dir_dientes}/id_dientes.dat', 'w') as id_dientes:
                    id_dientes.write( text_ready[:-1] )
            else:
                pass
        else:
            pass
    else:
        pass


def remove_id(id=None, superdel=False):
    '''Dar de baja un paciente'''
    list_pacientes = get_pacientes()
    if (
        not list_pacientes == None and
        not id == None
    ):
        print(list_pacientes)
        paciente_csv = f'{dir_dientes}/paciente.csv'
        with open(paciente_csv, 'w') as text_csv:
            text_csv.write('')
            
        for paciente in list_pacientes:
            the_id = paciente[0]
            name = paciente[1]
            remove = paciente[2]
            date = paciente[3]
            if id == paciente[0]:
                if not paciente[2] == 1:
                    remove = 1
                else:
                    pass#remove = paciente[2]
            else:
                pass
            with open(
                paciente_csv, 'a', newline=''
            ) as text_csv:
                writer_csv = csv.writer(text_csv, delimiter=',')
                writer_csv.writerow(
                    [
                    int(the_id),
                    str(name),
                    int(remove),
                    str(date)
                    ]
                )

        # Reiniciar parametros a los default en "id_dientes.dat"
        id_dientes_archive = get_data(mode_dict=False)
        text_ready = ''
        for line in id_dientes_archive.split('\n'):
            if line.startswith('current_id='):
                line = f'current_id='
            elif line.startswith('current_id_name='):
                line = f'current_id_name='
            else:
                pass
            text_ready += line + '\n'
        
        with open(f'{dir_dientes}/id_dientes.dat', 'w') as id_dientes:
            id_dientes.write( text_ready[:-1] )


def get_section_color(diente=1.8, section=1):
    '''Obtener el color de una seccion especifica del diente'''
    section=int(section)

    diente_sections = get_diente(diente=diente)
    if not diente_sections == None:
        return_section = None
        for diente_section in diente_sections:
            if int(diente_section[0]) == section:
                return_section = diente_section[1]
            else:
                pass
        if return_section == 'None':
            return_section = None
        else:
            pass
        return return_section
    else:
        return None


def get_diente(diente=1.8):
    '''Obtener la informacion de un diente'''
    diente = f'{get_id_dir()}/diente_{diente}.csv'
    if os.path.isfile(diente):
        with open(diente, 'r', newline='') as info_diente:
            text_diente = csv.reader(info_diente)
            list_diente = []
            for line in text_diente:
                print(
                    f'{type( int(line[0]) )} {line[0]}\n'
                    f'{type( line[1] )} {line[1]}\n'
                )
                list_diente.append( [ line[0], line[1] ] )
                #list_diente.append( f'{line[0]}={line[1]}' )
            return list_diente
    else:
        return None


def save_diente(number=1.8, section=0, color=None):
    '''Guardar la informacion de un diente'''
    #Guardar info
    diente_csv = f'{get_id_dir()}/diente_{number}.csv'
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
                        f'{section},{color}'
                    ).rstrip('\r\n') + '\n' + text
                )
        else:
            writer_csv = csv.writer(info_text, delimiter=',')
            writer_csv.writerow(
                [
                str(section),
                str(color)
                ]
            )
    df = pd.read_csv(
        f'{get_id_dir()}/diente_{number}.csv',  sep=',', header=None
    )
    csv_final = df.drop_duplicates(0)
    csv_final.to_csv(
        f'{get_id_dir()}/diente_{number}.csv',
        sep=',',
        header=None, index=False
    )
    print(csv_final)