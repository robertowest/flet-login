from flet import *


class MyUserBar(UserControl):
    dlg_modal = None

    def __init__(self, page, fusuario):
        super().__init__()
        self.page = page
        self.usuario = fusuario

    def close_dlg(self, e):
        self.dlg_modal.open = False
        self.page.update()

    def open_dlg_modal(self, e):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def build(self):
        self.dlg_modal = AlertDialog(
            bgcolor=colors.WHITE,
            modal=True,
            title=Text("Código QR",
                       style=TextStyle(
                           color="black",
                       )),
            content=Icon(
                icons.QR_CODE_2,
                color=colors.BLACK,
                size=250
            ),
            actions=[
                TextButton(
                    content=Text(
                        value="Cerrar",
                        weight=FontWeight.W_600
                    ),
                    style=ButtonStyle(
                        color="blue",
                    ),
                    on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Ha cerrado el modal Dlg"),
        )

        my_user_bar = Container(
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.bottom_right,
                colors=["#ec008c", "#fc6767"]
            ),
            width=self.page.window_max_width,
            height=56,
            content=Row(
                [
                    Column(
                        [
                            Container(
                                width=50,
                                height=56,
                                margin=margin.only(left=-5),
                                content=Icon(icons.PEOPLE_ALT,
                                             color=colors.WHITE,
                                             size=20)
                            )
                        ]

                    ),
                    Column(
                        [
                            Container(
                                width=200,
                                padding=5,
                                content=Text(
                                    f"{self.usuario}",
                                    style=TextStyle(
                                        size=16,
                                        color=colors.WHITE,
                                        weight=FontWeight.W_600)
                                )
                            )
                        ], alignment=MainAxisAlignment.CENTER,
                    ),
                    Column(
                        [
                            Container(
                                width=60,
                                height=56,
                                margin=margin.only(left=55),
                                content=IconButton(
                                    content=Icon(
                                        icons.QR_CODE,
                                        color=colors.WHITE,
                                        size=40
                                    ), on_click=self.open_dlg_modal
                                ),
                            )
                        ], alignment=MainAxisAlignment.END

                    ),
                ], alignment=MainAxisAlignment.SPACE_AROUND
            ),
        )

        return my_user_bar
