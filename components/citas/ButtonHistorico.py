from flet import *


class MyButtonHistorico(UserControl):
    def __init__(self, ftexto, ficon):
        super().__init__()
        self.texto = ftexto
        self.icon = ficon

    def build(self):
        historico_button = Container(
            margin=margin.only(top=50),
            content=ElevatedButton(icon=self.icon,
                                   text=self.texto,
                                   width=150,
                                   color=colors.WHITE,
                                   bgcolor=colors.RED_600,
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

        return historico_button
