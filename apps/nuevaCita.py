from flet import *
from flet_route import Params, Basket
from components.AppBar import MyAppBar
from components.UserBar import MyUserBar
from components.Background import MyBackground
from components.NavigationBar import MyNavigationBar
from components.citas.CardClinica import MyCardClinica


class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    BLUE_LIGHT = "#428aed"
    BLUE_DARK = "#5d7ae5"
    DARK_BLUE = "#0024ed"
    GRAY_LIGHT = "#f0f2fc"
    SOFT_BLUE = "#6f8dde"


class Styles:
    TEXT_COLOR = Colors.WHITE
    TEXT_SIZE = 16
    BUTTON_COLOR = Colors.BLACK


def NuevaCita(page: Page, params: Params, basket: Basket):
    def obtenerDatos():
        datos = page.client_storage.get("data")
        return datos['Data']

    cardAldaia = MyCardClinica(page, "Clínica Aldaia", "C/ Xest, 32", "Aldaia",
                               "./assets/clinica/aldaia.webp")

    cardTorrent = MyCardClinica(page, "Clínica Torrent", "Avda. Juan Carlos I, 12", "Torrent",
                               "./assets/clinica/torrent.webp")

    cardEliana = MyCardClinica(page, "Clínica El Osito", "C/ Tuéjar, 37 Local 3B", "L'Eliana",
                                "./assets/clinica/eliana.webp")

    cardAlfafar = MyCardClinica(page, "Clínica Alfafar", "CC Parque Albufera", "Alfafar",
                                "./assets/clinica/alfafar.webp")

    cita = Container(
        width=page.window_max_width,
        height=page.window_max_height,
        margin=0,
        padding=20,
        content=Column(
            [
                cardAldaia,
                cardTorrent,
                cardEliana,
                cardAlfafar,

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,

        )
    )

    imagen = Container(
        width=page.window_max_width,
        height=page.window_height / 1.5,
        padding=0,
        margin=0,
        content=Column(
            [
                Image(
                    src="./assets/atenea.png",
                    width=300,
                    height=300,
                    fit=ImageFit.CONTAIN,
                    opacity=0.1,
                ),
            ], alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    background = MyBackground()

    stack = Stack(
        [
            background.build(),
            imagen,
            cita
        ],
        width=page.window_max_width,
        height=page.window_max_height,
    )

    header = MyAppBar("SELECCIONE CLÍNICA", icons.MENU, "")
    user_bar = MyUserBar(page, f"{obtenerDatos()['Nomb']} {obtenerDatos()['Apel1']} {obtenerDatos()['Apel2']}")
    navigation_bar = MyNavigationBar(page, 1)

    page.title = "Nuevas citas"
    theme = Theme()
    theme.page_transitions.android = PageTransitionTheme.NONE
    theme.page_transitions.ios = PageTransitionTheme.NONE
    theme.page_transitions.macos = PageTransitionTheme.NONE
    theme.page_transitions.linux = PageTransitionTheme.NONE
    theme.page_transitions.windows = PageTransitionTheme.NONE
    page.theme = theme
    print("Ruta login:", page.route)

    return View(
        '/nueva_cita',
        [
            header.build(),
            user_bar.build(),
            stack,
            navigation_bar.build()
        ],
        padding=0,
        spacing=0
    )
