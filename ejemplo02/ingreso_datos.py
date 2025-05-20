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

# Leemos el txt con csv, con codificacion utf-8
with open('data/datos_clubs.txt', newline='', encoding='utf-8') as f:
    # Delimitamos cada item de la linea con ; ya que ese es el formato del archivo
    lector = csv.reader(f, delimiter=';')
    # lector es un iterador de las lineas, pero lo trasnformamos a lista, para poder recorrerla.
    datos_clubs = list(lector)
    # print(datos_clubs)
    # Por cada linea (club) creamos un nuevo club, asignando los valores correspondientes, cada objeto dentro de la lista, es otra lista
    # por eso podemos acceder a sus posiciones.
    for datos in datos_clubs:
        club = Club(nombre=datos[0], deporte=datos[1], fundacion=datos[2])
    # Finalmente agreagmos cada objeto creado.
        session.add(club)

# Seguimos el mismo procedimiento de lectura que el archivo anterior.
with open('data/datos_jugadores.txt', newline='', encoding='utf-8') as f:
    # El lector contiene un iterador, lo trasnformamos a lista, para poder recorrerlo en un for.
    lector = csv.reader(f, delimiter=';')
    datos_jugadores = list(lector)
    # print(datos_jugadores)
    for datos in datos_jugadores:
        # Por cada linea, hacemos una consulta a la BD, la cual connsiste en buscar el nombre de un club que coincida
        # con el valor del club que viene en los datos del jugador
        # para así obtener el identificador del club, que asignaremos
        # como foreign key cuando creemos a los jugadores.

        club = session.query(Club).filter_by(nombre=datos[0]).one()
        # print(club.id)
        # print(datos)

        # Creamos cada jugador, asignando los valores respextivos, y en la parte del club_id,
        # accedemos y asignamos el id del club que ya consultamos anteriormente
        jugador = Jugador(nombre=datos[3], dorsal=datos[2], posicion=datos[1], club_id=club.id)
        session.add(jugador)

session.commit()
