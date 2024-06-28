from flet import *


class MyNavigationBar(UserControl):
    def __init__(self, page, index):
        super().__init__()
        self.page = page
        self.selected_index = index

    def change_page(self, e, page):
        print(page.route)
        print(e.control.selected_index)

        # self.selected_index = e.control.selected_index

        if e.control.selected_index == 0:
            page.go("/home")
        if e.control.selected_index == 1:
            page.go("/nueva_cita")
        if e.control.selected_index == 2:
            page.go("/historico")

        page.update()

    def build(self):
        navigation_bar = NavigationBar(
            bgcolor="#2a68f7",
            shadow_color=colors.DEEP_PURPLE,
            selected_index=self.selected_index,
            indicator_color="#2251bf",
            on_change=lambda e: self.change_page(e, self.page),
            destinations=[
                NavigationDestination(icon=icons.CALENDAR_MONTH, label="Citas pendientes"),
                NavigationDestination(icon=icons.ADD, label="Nueva cita"),
                NavigationDestination(icon=icons.LIST, label="Histórico de citas"),

            ]
        )

        return navigation_bar
