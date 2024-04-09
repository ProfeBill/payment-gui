from kivy.app import App


from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

# Logica de la tarjeta de credito
from CreditCard.Payments import CreditCardCalculator

class PaymentApp(App):
    def build(self):
        contenedor = GridLayout(cols=2,padding=20,spacing=20)

        contenedor.add_widget( Label(text="Valor de la compra") )
        self.compra = TextInput(font_size=30 )
        contenedor.add_widget(self.compra)

        contenedor.add_widget( Label(text="Número de cuotas") )
        self.cuotas = TextInput(font_size=30 )
        contenedor.add_widget(self.cuotas)

        contenedor.add_widget( Label(text="Tasa de Interés") )
        self.tasa = TextInput(font_size=30 )
        contenedor.add_widget(self.tasa)

        self.resultado = Label()
        contenedor.add_widget(resultado)

        calcular = Button(text="Calcular",font_size=40)
        contenedor.add_widget(calcular)

        # Conectar con el callback con el evento press del boton
        calcular.bind( on_press=self.calcular_cuota )

        # Siempre se retorna el widget que contiene a todos los demás
        return contenedor
    
    # instance es el widget que generó el evento
    # value es el valor actual que tiene el widget
    def calcular_cuota( self, value ):
        try:
            self.resultado.text = CreditCardCalculator.calcPayment( float(self.compra.text), int(self.cuotas.text), float(self.interes.text) )
        except Exception as err:
            self.mostrar_error( err)

    def mostrar_error( self, err ):
        contenido = GridLayout(cols=1)
        contenido.add_widget( Label(text= str(err) ) )
        cerrar = Button(text="Cerrar" )
        contenido.add_widget( cerrar )
        popup = Popup(content=contenido)
        cerrar.bind( on_press=popup.dismiss)
        popup.open()


if __name__ == "__main__":
    PaymentApp().run()