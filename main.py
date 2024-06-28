from flet import *
from flet_route import *

from views.login import Login
from views.registro import Registro
from apps.home import Home
from apps.nuevaCita import NuevaCita
from apps.historico import HistoricoCita


def main(page: Page):
    page.padding = 0
    page.spacing = 0
    page.window_width = 390
    page.window_height = 844
    page.window_max_width = 800
    page.window_max_height = 844
    page.window_left = 1500

    page.fonts = {
        "Poppins": "https://fonts.google.com/share?selection.family=Onest:wght@100..900"
    }
    page.theme = Theme(font_family="Poppins")
    page.theme_mode = ThemeMode.DARK

    theme = Theme()
    theme.page_transitions.android = PageTransitionTheme.ZOOM
    theme.page_transitions.ios = PageTransitionTheme.ZOOM
    theme.page_transitions.macos = PageTransitionTheme.ZOOM
    theme.page_transitions.linux = PageTransitionTheme.ZOOM
    theme.page_transitions.windows = PageTransitionTheme.ZOOM
    page.theme = theme

    page.update()

    app_routes = [
        path('/', clear=True, view=Login),
        path('/registro', clear=True, view=Registro),
        path('/home', clear=True, view=Home, ),
        path('/nueva_cita', clear=True, view=NuevaCita),
        path('/historico', clear=True, view=HistoricoCita),
    ]
    Routing(page=page, app_routes=app_routes)
    page.go(page.route)


if __name__ == '__main__':
    # app(target=main, view=WEB_BROWSER, assets_dir="assets")  # en web
    app(target=main, assets_dir="assets")  # en pantalla
