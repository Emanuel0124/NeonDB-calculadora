import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

# Logica de la tarjeta de credito
from Logica_declaración import Logica

class PaymentApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)
        
        contenedor.add_widget(Label(text="Ingresa tus ingresos laborales"))
        self.ingresos_laborales = TextInput(font_size=30)
        contenedor.add_widget(self.ingresos_laborales)
        
        contenedor.add_widget(Label(text="otros ingresos"))
        self.otros_ingresos = TextInput(font_size=30)
        contenedor.add_widget(self.otros_ingresos)
        
        contenedor.add_widget(Label(text="retenciones en la fuente"))
        self.retenciones_fuente = TextInput(font_size=30)
        contenedor.add_widget(self.retenciones_fuente)
        
        contenedor.add_widget(Label(text="seguridad social"))
        self.seguridad_social = TextInput(font_size=30)
        contenedor.add_widget(self.seguridad_social)
        
        contenedor.add_widget(Label(text="Aportes de pension"))
        self.aportes_pension = TextInput(font_size=30)
        contenedor.add_widget(self.aportes_pension)
        
        contenedor.add_widget(Label(text="gastos en creditos hipotecarios"))
        self.gastos_creditos_hipotecarios = TextInput(font_size=30)
        contenedor.add_widget(self.gastos_creditos_hipotecarios)
        
        contenedor.add_widget(Label(text="Donaciones"))
        self.donaciones = TextInput(font_size=30)
        contenedor.add_widget(self.donaciones)
        
        contenedor.add_widget(Label(text="Gastos en educacion|"))
        self.gastos_educacion = TextInput(font_size=30)
        contenedor.add_widget(self.gastos_educacion)
        
        self.resultado = Label()
        contenedor.add_widget(self.resultado)
        
        calcular = Button(text="Calcular", font_size=40)
        contenedor.add_widget(calcular)
        
        # Conectar con el callback con el evento press del boton
        calcular.bind(on_press=self.calcular_renta)
        
        # Siempre se retorna el widget que contiene a todos los demás
        return contenedor
    
    def calcular_renta(self, instance):
        try:
            self.result = Logica.calcular_impuesto_renta(
                float(self.ingresos_laborales.text),
                float(self.otros_ingresos.text),
                float(self.retenciones_fuente.text),
                float(self.seguridad_social.text),
                float(self.aportes_pension.text),
                float(self.gastos_creditos_hipotecarios.text),
                float(self.donaciones.text),
                float(self.gastos_educacion.text)
            )
            self.resultado.text = f"El impuesto a pagar es: {self.result}"
        except Exception as err:
            self.mostrar_error(err)
    
    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
        popup = Popup(content=contenido)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    PaymentApp().run()





"""
def obtener_numero_input(mensaje):
    
    #Solicita al usuario un valor numérico para un mensaje dado.
    
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

ingresos_laborales = obtener_numero_input("Ingrese los ingresos laborales en el año: ")
otros_ingresos = obtener_numero_input("Ingrese el valor de otros ingresos en el año: ")
retenciones_fuente = obtener_numero_input("Ingrese el valor de retenciones en la fuente en el año: ")
seguridad_social = obtener_numero_input("Ingrese los pagos de seguridad social en el año: ")
aportes_pension = obtener_numero_input("Ingrese los aportes a la pensión en el año: ")
gastos_creditos_hipotecarios = obtener_numero_input("Ingrese el valor de los pagos de créditos hipotecarios en el año: ")
donaciones = obtener_numero_input("Ingrese el valor de las donaciones en el año: ")
gastos_educacion = obtener_numero_input("Ingrese el valor de los gastos en educación en el año: ")

print("Procesando...")

result = Logica.calcular_impuesto_renta(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)


"""

import os

