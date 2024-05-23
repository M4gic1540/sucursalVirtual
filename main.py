import flet as ft
from manager import Manager

class Form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        self.manager = Manager()

        #Configuracion de campos

        self.name = ft.TextField(label="Nombre", border_color="#C0C0C0")
        self.last_name = ft.TextField(label="Apellido", border_color="#C0C0C0")
        self.rut = ft.TextField(label="Rut", border_color="#C0C0C0",
                                input_filter=ft.NumbersOnlyInputFilter(),
                                max_length=13)

        self.email = ft.TextField(label="Email", border_color="#C0C0C0")
        self.phone = ft.TextField(label="Telefono", border_color="#C0C0C0",
                                  input_filter=ft.TextOnlyInputFilter(),
                                  max_length=9)

        self.search_field = ft.TextField(label="Buscar por alumno", suffix_icon=ft.icons.SEARCH, border= ft.InputBorder.UNDERLINE, label_style=ft.TextStyle(color="#062E1F"), border_color="#062E1F",color="#062E1F")

        #Contruccion de datatable

        self.data_table = ft.DataTable(
            expand=True,
            border= ft.border.all(2, "#062E1F"),
            data_row_color={ft.MaterialState.SELECTED: "#062E1F",
                            ft.MaterialState.PRESSED: "#062E1F"},
            border_radius=10,
            show_checkbox_column=True,

            columns=[
                ft.DataColumn(ft.Text("Nombre", color="#062E1F", weight="bold")),
                ft.DataColumn(ft.Text("Apellido", color="#062E1F",weight="bold")),
                ft.DataColumn(ft.Text("Rut", color="#062E1F", weight="bold")),
                ft.DataColumn(ft.Text("Email", color="#062E1F", weight="bold")),
                ft.DataColumn(ft.Text("Telefono", color="#062E1F", weight="bold"),numeric=True),
            ] 
        )

        #Configuracion de contenedores
        self.form = ft.Container( #Configuracion de formulario 
            bgcolor="#062E1F",
            border_radius=10,
            col=4,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Ingrese Sus Datos", color="white", size=40,
                            text_align="center", font_family="Calibri", weight="bold"),
                    self.name,
                    self.last_name,
                    self.rut,
                    self.email,
                    self.phone,
                    ft.Container(
                        content= ft.Row(
                            controls=[
                                ft.TextButton(text="Guardar", icon=ft.icons.SAVE, style=ft.ButtonStyle(color="#C0C0C0", bgcolor="#062E1F")),
                                ft.TextButton(text="Actualizar", icon=ft.icons.UPDATE, style=ft.ButtonStyle(color="#C0C0C0", bgcolor="#062E1F")),
                                ft.TextButton(text="Borrar", icon=ft.icons.DELETE, style=ft.ButtonStyle(color="#C0C0C0", bgcolor="#062E1F")),
                            ]
                        )
                    )
                ]
            )
        )

        self.table = ft.Container( #Configuracion de tabla
            col=8,
            border_radius=5,
            bgcolor="#C0C0C0", #opcional para opciones de menu de tabla
            content= ft.Column(
                controls=[
                    ft.Container(
                        padding= 10,
                        #bgcolor="#062E1F",
                        content=ft.Row(
                            controls=[
                                self.search_field,
                                ft.IconButton(tooltip="Descargar PDF", icon=ft.icons.PICTURE_AS_PDF, icon_color="#062E1F"),
                                ft.IconButton(tooltip="Descargar Excel", icon=ft.icons.SAVE_ALT, icon_color="#062E1F"),
                            ]
                        )
                    ),
                    ft.Column(
                        expand=True,
                        scroll="auto",
                        controls=[
                            self.data_table,
                        ]
                    )
                ]
            )
        )

        self.content = ft.ResponsiveRow(
            controls=[
                self.form,
                self.table
            ]
        )

    def show_data(self):
        self.data_table.rows = []
        for student in self.manager.get_student():
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(student[1])),
                        ft.DataCell(ft.Text(student[2])),
                        ft.DataCell(ft.Text(str(student[3]))),
                        ft.DataCell(ft.Text(student[4])),
                        ft.DataCell(ft.Text(str(student[5]))),
                    ]
                )
            )
            
    

    def build(self):
        return self.content


def main(page: ft.Page):
    page.title = "SUCURSAL VIRTUAL"
    page.bgcolor = "black"
    page.window_min_height = 720
    page.window_min_width = 1280

    page.add(Form())


ft.app(main)
