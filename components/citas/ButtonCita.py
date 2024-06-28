from flet import *


class MyButtonCita(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        nueva_cita = Container(
            margin=margin.only(top=50),
            content=ElevatedButton(icon=icons.ADD,
                                   text=" NUEVA CITA",
                                   color=colors.WHITE,
                                   bgcolor=colors.RED_600,
                                   on_click=lambda _: self.page.go('/nueva_cita'),
                                   style=ButtonStyle(
                                       shadow_color=colors.BLACK,
                                       padding=10,
                                       side={
                                           MaterialState.DEFAULT: BorderSide(2, colors.RED_ACCENT_200),
                                           MaterialState.HOVERED: BorderSide(4, colors.RED_ACCENT_200),
                                       },
                                       shape={
                                           MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                           MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                                       },
                                   )
                                   ),
        )

        return nueva_cita
