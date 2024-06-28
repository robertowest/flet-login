from flet import *
from flet_route import Params, Basket
from components.AppBar import MyAppBar
from components.UserBar import MyUserBar
from components.Background import MyBackground
from components.NavigationBar import MyNavigationBar
from components.citas.Card import MyCard
from components.citas.ButtonCita import MyButtonCita


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


def Home(page: Page, params: Params, basket: Basket):
    def obtenerDatos():
        datos = page.client_storage.get("data")
        return datos['Data']

    def obtenerCitas():
        citas = obtenerDatos()['Citas']
        lista_citas = citas[0]
        print(lista_citas)
        return lista_citas

    card = MyCard(page, obtenerCitas()['Especialidad'], "Clínica de L'Eliana", obtenerCitas()['Especialista'],
                  f"{obtenerCitas()['Fecha']} - {obtenerCitas()['hora']}:{obtenerCitas()['minuto']} h. ",
                  obtenerCitas()['VisitTypeName'])

    button_cita = MyButtonCita(page)

    home = Container(
        width=page.window_max_width,
        height=page.window_max_height,
        margin=0,
        padding=20,
        content=Column(
            [
                card.build(),
                button_cita.build()
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
            home,
        ],
        width=page.window_max_width,
        height=page.window_max_height,
    )

    header = MyAppBar("PRÓXIMAS CITAS", icons.MENU, "")
    user_bar = MyUserBar(page, f"{obtenerDatos()['Nomb']} {obtenerDatos()['Apel1']} {obtenerDatos()['Apel2']}")
    navigation_bar = MyNavigationBar(page, 0)

    page.title = "Próximas citas"
    theme = Theme()
    theme.page_transitions.android = PageTransitionTheme.ZOOM
    theme.page_transitions.ios = PageTransitionTheme.ZOOM
    theme.page_transitions.macos = PageTransitionTheme.ZOOM
    theme.page_transitions.linux = PageTransitionTheme.ZOOM
    theme.page_transitions.windows = PageTransitionTheme.ZOOM
    page.theme = theme
    print("Ruta login:", page.route)

    return View(
        '/home',
        [
            header.build(),
            user_bar.build(),
            stack,
            navigation_bar.build()
        ],
        padding=0,
        spacing=0
    )
