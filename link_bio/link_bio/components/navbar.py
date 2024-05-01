import reflex as rx # type: ignore

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Juarito",
            height="40px"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )