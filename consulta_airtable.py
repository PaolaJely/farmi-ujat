import flet as ft
import nube as nb
import main as m


def main(page: ft.Page):
    def boton_regreso(e: ft.ControlEvent):
        page.clean()
        m.main(page)

    page.title = "Recetas"
    page.theme_mode = "light"
    page.scroll = True
    page.appbar = ft.AppBar(
        title= ft.Text("Listado de medicamentos UJAT"),
        leading=ft.Icon("LIST_ALT", color=ft.Colors.WHITE),
        bgcolor="blue",
        center_title=True,
        actions=[
        ft.TextButton(
            text="Regresar",
            icon="KEYBOARD_RETURN",
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                padding=10,
            ),
            on_click=boton_regreso
        )
    ]
    )

#Compomponentes de la pagina
    encabezado = [
        ft.DataColumn(ft.Text("Medicamento")),
        ft.DataColumn(ft.Text("Interacciones"))
    ]
    filas = []
    datos = nb.Receta.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.medicamento))
        celda2 = ft.DataCell(ft.Text(d.interacciones))
        fila = ft.DataRow([celda1,celda2])
        filas.append(fila)

    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_medicamentos)
    page.update()
#agregar a todos los archivos
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)