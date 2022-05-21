from dash import html


def indicator(value, title, percentage):
    if percentage > 0:
        angle = "up"
    elif percentage < 0:
        angle = "down"
    else:
        angle = "right"
    return html.Div(
        [
          html.Div([
              html.I(className=f"fa-solid fa-arrow-{angle}"),
              html.Span(f"%{percentage}")
          ], className="flex items-center border border-red w-1/4 ")
        ],
        className="flex space-x-1 w-full text-red"
    )
