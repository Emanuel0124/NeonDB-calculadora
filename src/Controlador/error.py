from controller import conectar_db
import psycopg2
from Logica_declaración import Logica

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (Exception, psycopg2.Error) as error:
            print(f"Error en la función {func.__name__}: {error}")
            conn = conectar_db()
            if conn:
                conn.rollback()  # Revertir la transacción en caso de error
                conn.close()
    return wrapper

@handle_error
def agregar_usuario_y_liquidacion(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                # Agregar usuario
                salario = ingresos_laborales + otros_ingresos
                sql_usuario = "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID_Usuario"
                cur.execute(sql_usuario, ('Nombre', 'Apellido', 'Documento', 'correo@ejemplo.com', '123456789', '2024-05-15', '2024-05-15', salario))
                id_usuario = cur.fetchone()[0]

                # Calcular impuesto de renta
                impuesto_renta = Logica.calcular_impuesto_renta(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)

                # Agregar liquidación con impuesto de renta
                sql_liquidacion = "INSERT INTO liquidacion (Indemnizacion, Vacaciones, Cesantias, Intereses_Sobre_Cesantias, Prima_Servicios, Retencion_Fuente, Total_A_Pagar, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql_liquidacion, (0, 0, 0, 0, 0, impuesto_renta, 0, id_usuario))

                conn.commit()
            conn.close()
            print("Usuario y liquidación agregados correctamente.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al agregar el usuario y la liquidación: {error}")

# Llamada a la función para agregar usuario y liquidación con los valores obtenidos del primer código
agregar_usuario_y_liquidacion(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)
