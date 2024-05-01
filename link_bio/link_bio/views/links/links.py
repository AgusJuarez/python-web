import reflex as rx #type: ignore
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Gmail", "https://reflex.dev"),
        link_button("Discord", "https://reflex.dev"),
        link_button("Steam", "https://reflex.dev"),
        link_button("GitHub", "https://reflex.dev"),
    )