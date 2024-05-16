import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import psycopg2
import database

# Función para conectar a la base de datos
def conectar_db():
    try:
        conn = psycopg2.connect(
            host=database.PGHOST,
            database=database.PGDATABASE,
            user=database.PGUSER,
            password=database.PGPASSWORD
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        return None

# Función para agregar un nuevo usuario con sus datos de ingresos
def agregar_usuario_y_liquidacion(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                # Agregar usuario
                sql_usuario = "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID_Usuario"
                cur.execute(sql_usuario, ('Nombre', 'Apellido', 'Documento', 'correo@ejemplo.com', '123456789', '2024-05-15', '2024-05-15', ingresos_laborales + otros_ingresos))
                id_usuario = cur.fetchone()[0]

                # Agregar liquidación
                sql_liquidacion = "INSERT INTO liquidacion (Indemnizacion, Vacaciones, Cesantias, Intereses_Sobre_Cesantias, Prima_Servicios, Retencion_Fuente, Total_A_Pagar, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql_liquidacion, (0, 0, 0, 0, 0, retenciones_fuente, 0, id_usuario))

                conn.commit()
            conn.close()
            print("Usuario y liquidación agregados correctamente.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al agregar el usuario y la liquidación: {error}")

# Función para consultar los datos de un usuario
def consultar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                # Consultar datos del usuario
                sql = "SELECT * FROM usuarios WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                usuario = cur.fetchone()
                
                # Consultar datos de la liquidación
                sql = "SELECT * FROM liquidacion WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                liquidacion = cur.fetchone()
                
                if usuario:
                    print("Datos del usuario:")
                    print(f"ID_Usuario: {usuario[0]}")
                    print(f"Nombre: {usuario[1]}")
                    print(f"Apellido: {usuario[2]}")
                    print(f"Documento_Identidad: {usuario[3]}")
                    print(f"Correo_Electronico: {usuario[4]}")
                    print(f"Telefono: {usuario[5]}")
                    print(f"Fecha_Ingreso: {usuario[6]}")
                    print(f"Fecha_Salida: {usuario[7]}")
                    print(f"Salario: {usuario[8]}")
                    
                    if liquidacion:
                        print("\nDatos de la liquidación:")
                        print(f"Indemnización: {liquidacion[1]}")
                        print(f"Vacaciones: {liquidacion[2]}")
                        print(f"Cesantías: {liquidacion[3]}")
                        print(f"Intereses sobre cesantías: {liquidacion[4]}")
                        print(f"Prima de servicios: {liquidacion[5]}")
                        print(f"Retención en la fuente: {liquidacion[6]}")
                        print(f"Total a pagar: {liquidacion[7]}")
                else:
                    print("No se encontró el usuario.")
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al consultar el usuario: {error}")

# Llamada a la función para agregar usuario y liquidación con los valores obtenidos del primer código
otros_ingresos = 0  
ingresos_laborales = 0  
retenciones_fuente = 0  
seguridad_social = 0  
aportes_pension = 0  
gastos_creditos_hipotecarios = 0  
donaciones = 0  
gastos_educacion = 0  
agregar_usuario_y_liquidacion(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)
