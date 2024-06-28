import requests
from flet import *
from flet_route import Params, Basket
from views.encryption import Encrypt


class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    BLUE_LIGHT = "#428aed"
    BLUE_DARK = "#5d7ae5"
    DARK_BLUE = "#0024ed"
    GRAY_LIGHT = "#f0f2fc"


class Styles:
    TEXT_COLOR = Colors.WHITE
    TEXT_SIZE = 16
    BUTTON_COLOR = Colors.BLACK


def login_api(usuario, password):
    url = "https://integraciones.clinica-atenea.com:58000/api/v1/app/Login"
    auth = {
        "DNI": usuario,
        "Pwd": password,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=auth)
    return response


def Login(page: Page, params: Params, basket: Basket):
    def print_respuesta(response):
        print(response.status_code)
        if response.status_code == 200:
            page.client_storage.set("data", response.json())
            page.go('/home')

    def text_button_container(text, on_click):
        return Container(
            content=TextButton(
                text,
                style=ButtonStyle(color=Styles.BUTTON_COLOR),
                on_click=on_click,
            )
        )

    def calcular_ancho(percentage):
        return page.window_width * percentage

    def button_clicked(e):
        usuario = usuario_textfield.value
        password = password_textfield.value

        encrypted = Encrypt.my_encrypt(password)
        print("Pass encriptado:", encrypted)
        decrypted = Encrypt.my_decrypt(encrypted)
        print("Pass desencriptado:", decrypted)

        # 5BF9a3+U9Wg=

        print("Usuario ingresado:", usuario)
        print("Contraseña ingresada:", encrypted)

        respuesta = login_api(usuario, encrypted)
        print_respuesta(respuesta)

    usuario_textfield = TextField(
        width=calcular_ancho(0.6),
        label_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL, size=14),
        hint_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL, size=14),
        label="Usuario",
        hint_text='DNI / NIF / Pasaporte',
        color=Colors.WHITE,
        height=40,
        content_padding=10,
        border_color=Colors.WHITE,
        border_radius=10,
        prefix_icon=icons.PERSON,
    )

    password_textfield = TextField(
        width=calcular_ancho(0.6),
        label_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL, size=14),
        label="Contraseña",
        height=40,
        content_padding=10,
        border_color=Colors.WHITE,
        border_radius=10,
        color=Colors.WHITE,
        prefix_icon=icons.LOCK,
        password=True,
        can_reveal_password=True
    )

    login = Container(
        width=page.window_width,
        height=page.window_height,
        margin=0,
        padding=0,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[Colors.BLUE_DARK, Colors.BLUE_LIGHT, Colors.GRAY_LIGHT],
        ),
        content=Column(
            controls=[
                Row(
                    [
                        Container(
                            margin=margin.only(top=100, bottom=50),
                            content=Image(
                                src='./assets/logo.png',
                                width=150,

                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(bottom=10),
                            content=usuario_textfield

                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            content=password_textfield
                        )

                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(top=50),
                            content=ElevatedButton("INICIAR SESIÓN",
                                                   width=calcular_ancho(0.6),
                                                   on_click=button_clicked,
                                                   color=Colors.WHITE,
                                                   bgcolor=colors.RED_600,
                                                   style=ButtonStyle(
                                                       shape={
                                                           MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                                           MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                                       },
                                                   )
                                                   ),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(top=50),
                            content=text_button_container('¿RECUPERAR CONTRASEÑA?', lambda _: page.go('/')),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            content=text_button_container('REGISTRARSE', lambda _: page.go('/registro')),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            ],
        )
    )
    page.title = "Iniciar sesión"
    page.theme = Theme(color_scheme_seed="blue")
    theme = Theme()
    theme.page_transitions.android = PageTransitionTheme.ZOOM
    theme.page_transitions.ios = PageTransitionTheme.ZOOM
    theme.page_transitions.macos = PageTransitionTheme.ZOOM
    theme.page_transitions.linux = PageTransitionTheme.ZOOM
    theme.page_transitions.windows = PageTransitionTheme.ZOOM
    page.theme = theme
    print("Ruta login:", page.route)

    return View(
        '/',
        [
            login
        ],
        padding=0

    )
