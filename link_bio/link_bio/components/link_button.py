import reflex as rx #type: ignore

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True
    )
    
    