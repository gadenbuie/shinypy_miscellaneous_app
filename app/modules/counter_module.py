from shiny import ui, module, render, reactive

# Module UI function
@module.ui
def counter_ui(increment):
     # Create namespace for IDs
    return ui.div(
        ui.input_action_button("button", f"Add {increment}"),
        ui.output_text("value"),
        ui.tags.br(),
        ui.output_text("total_clicks")
    )

# Module server function
@module.server
def counter_server(input, output, session, increment):
    @reactive.calc
    def count():
        return input.button() * increment

    @output
    @render.text
    def value():
        return f"Current value: {count()}"
    
    @output
    @render.text
    def total_clicks():
        return f"Number of clicks: {input.button()}"