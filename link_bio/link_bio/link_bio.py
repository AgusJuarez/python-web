import reflex as rx # type: ignore

class State(rx.State):
    pass
    
def index() -> rx.Component:
    return rx.text("Hola Reflex!", color="blue")

app = rx.App()
app.add_page(index)
app.compile()