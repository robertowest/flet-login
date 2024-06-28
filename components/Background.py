from flet import *
import math


class MyBackground(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        background = Container(
            margin=0,
            padding=20,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=Alignment(0.8, 1),
                colors=[
                    "#FFFFFF",
                    "#6e91f3",

                ],
                tile_mode=GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),

        )

        return background
