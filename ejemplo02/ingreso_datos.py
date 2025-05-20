import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_clubs.txt', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';')
    datos_clubs = list(lector)
    for datos in datos_clubs:
        club = Club(nombre=datos[0], deporte=datos[1], fundacion=datos[2])
        session.add(club)

with open('data/datos_jugadores.txt', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';')
    datos_jugadores = list(lector)

session.commit()
