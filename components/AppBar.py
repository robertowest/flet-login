from flet import *


class MyAppBar(UserControl):
    def __init__(self, ftexto, ficono, fsrc):
        super().__init__()
        self.texto = ftexto
        self.icono = ficono
        self.src = fsrc

    def build(self):
        my_app_bar = AppBar(
            leading=Icon(self.icono),
            leading_width=40,
            title=Text(f"{self.texto}",
                       style=TextStyle(
                           size=16
                       )),
            color=colors.WHITE,
            bgcolor="#2a68f7",

            actions=[
                IconButton(
                    content=Image(
                        src="./assets/logo.png",
                        width=80
                    ),
                ),

            ]
        )

        return my_app_bar
