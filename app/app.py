from shiny import App, ui
from modules.counter_module import counter_ui, counter_server

# Main app UI
app_ui = ui.page_fluid(
    ui.h2("Demonstration of Shiny Modules"),
    ui.row(
        ui.column(6,
            ui.card(
                "Counter 1 (increments by 1)",
                counter_ui("counter1", increment=1)
            )
        ),
        ui.column(6,
            ui.card(
                "Counter 2 (increments by 10)",
                counter_ui("counter2", increment=10)
            )
        )
    )
)

# Main app server
def server(input, output, session):
    # Initialize counter modules with different configurations
    counter_server("counter1", increment=1)
    counter_server("counter2", increment=10)

app = App(app_ui, server)