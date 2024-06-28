from flet import *


class MyCard(UserControl):
    def __init__(self, page, fespecialidad, fsede, fespecialista, ffecha, ftipo_visita):
        super().__init__()
        self.page = page
        self.especialidad = fespecialidad
        self.sede = fsede
        self.especialista = fespecialista
        self.fecha = ffecha
        self.tipo_visita = ftipo_visita

    def build(self):
        mycard = Container(
            width=self.page.window_width - 100,
            height=125,
            bgcolor=colors.WHITE70,
            border_radius=10,
            border=border.all(2, "#FFFFFF"),
            content=Column(
                [
                    Row(
                        [
                            Text(f"{self.especialidad}",
                                 color=colors.BLACK,
                                 weight=FontWeight.W_700,
                                 style=TextStyle(
                                     decoration=TextDecoration.UNDERLINE,
                                     decoration_color=colors.BLACK,
                                     decoration_thickness=1,
                                 )
                                 ),
                            Text(f"(Clínica de L'Eliana)",
                                 color=colors.BLACK,
                                 weight=FontWeight.W_700,
                                 ),

                        ], alignment=MainAxisAlignment.SPACE_EVENLY,
                        spacing=0,
                    ),
                    Row(
                        [
                            Text(f"{self.especialista}",
                                 color=colors.BLACK,
                                 italic=True,
                                 size=11)

                        ], alignment=MainAxisAlignment.CENTER,
                        spacing=0,
                    ),
                    Row(
                        [
                            Text(
                                f"{self.fecha}",
                                color=colors.BLACK,
                                size=12),
                            Text(
                                f"- {self.tipo_visita}",
                                color=colors.GREY_600,
                                size=12
                            ),
                        ], alignment=MainAxisAlignment.CENTER,
                        spacing=0,
                    ),
                    Row(
                        [
                            TextButton(
                                width=90,
                                height=30,
                                style=ButtonStyle(
                                    padding=5,
                                    bgcolor=colors.RED_600,
                                    shape={
                                        MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                        MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                    },
                                ),
                                content=Row(
                                    [
                                        Icon(name=icons.EDIT_OUTLINED, color=colors.WHITE, size=14),
                                        Text("CAMBIAR", size=12, color=colors.WHITE)
                                    ]
                                )
                            ),
                            TextButton(
                                width=90,
                                height=30,
                                style=ButtonStyle(
                                    padding=5,
                                    bgcolor=colors.RED_600,
                                    shape={
                                        MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                        MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                    },
                                ),
                                content=Row(
                                    [
                                        Icon(name=icons.DELETE, color=colors.WHITE, size=14),
                                        Text("ANULAR", size=12, color=colors.WHITE)
                                    ]
                                )
                            )
                        ], alignment=MainAxisAlignment.CENTER
                    )
                ]
            )
        )

        return mycard
