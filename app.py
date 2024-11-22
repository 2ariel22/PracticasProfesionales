import flet as ft
import time

def main(page: ft.Page):
    page.title = "Muro de Mensajes"
    page.window_width = 600
    page.window_height = 600
    page.padding = 20
    
    # Lista de mensajes
    messages = ft.ListView(
        expand=True,
        spacing=10,
        height=400,
        auto_scroll=True
    )

    def enviar_mensaje(e):
        if not txt_mensaje.value: return
        
        # Crear nuevo mensaje
        messages.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(time.strftime("%H:%M:%S")),
                    ft.Text(txt_mensaje.value, size=16)
                ]),
                bgcolor=ft.colors.BLUE_50,
                padding=10,
                border_radius=5,
            )
        )
        # Limpiar campo de texto
        txt_mensaje.value = ""
        page.update()

    # Campo para escribir mensaje
    txt_mensaje = ft.TextField(
        hint_text="Escribe tu mensaje aquí...",
        expand=True,
        multiline=False,
        on_submit=enviar_mensaje
    )

    # Botón enviar
    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensaje)

    # Construir la interfaz
    page.add(
        ft.Text("Muro de Mensajes", size=30, weight=ft.FontWeight.BOLD),
        ft.Text("¡Comparte tus mensajes con todos!", size=16),
        messages,
        ft.Row(
            controls=[
                txt_mensaje,
                btn_enviar
            ],
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)