import reflex as rx #type: ignore
import datetime
def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text("Esto es un hermoso y explendido footer donde futuramente colocare"),
        rx.link(f"cosas asombrosas en este {datetime.date.today().year}", 
                href="https://github.com/AgusJuarez", 
                is_external=True
                ),
        align="center"
    )