import reflex as rx #type: ignore
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Gmail","Contactate conmigo", "https://reflex.dev"),
        link_button("Discord","Tambien puedes encontrarme por aca", "https://reflex.dev"),
        link_button("Steam","No creo que quieras hablarme por este medio.... O si :eyes:", "https://reflex.dev"),
        link_button("GitHub","Por aqui puedes encontrar las cosas con las cuales voy aprendiendo", "https://reflex.dev"),
        width="100%"
    )