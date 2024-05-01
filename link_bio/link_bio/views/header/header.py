import reflex as rx #type: ignore

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AJ", size="4", radius="full"),
        rx.text("@agush_juarez"),
        rx.text("Muy buenas! Mi nombre es Agustin Juarez"),
        rx.text("Soy un estudiande en busca de experiencia en el mundo de la programación. Se me da bien el trabajo en equipo y me gusta estar siempre aprendiendo cosas nuevas que puedan aportar a mi formación profesional."),
        align="center"
    )
