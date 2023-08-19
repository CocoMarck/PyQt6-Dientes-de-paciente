import csv
import pandas as pd
import os


dir_dientes='info_dientes'


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
    diente = f'{dir_dientes}/diente_{diente}.csv'
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
    diente_csv = f'{dir_dientes}/diente_{number}.csv'
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
        f'info_dientes/diente_{number}.csv',  sep=',', header=None
    )
    csv_final = df.drop_duplicates(0)
    csv_final.to_csv(
        f'info_dientes/diente_{number}.csv',
        sep=',',
        header=None, index=False
    )
    print(csv_final)