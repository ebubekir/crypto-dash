from dash import html


def indicator(value, title, percentage, sub_value=None):
    text_styles = {
        "up": "text-green-400",
        "down": "text-red-400",
        "neutral": "text-stone-400"
    }
    if percentage > 0:
        angle = "up"
        style = text_styles['up']
    elif percentage < 0:
        angle = "down"
        style = text_styles['down']
    else:
        angle = "right"
        style = text_styles['neutral']
    return html.Div(
        [
            html.Div([
                html.I(className=f"fa-solid fa-arrow-{angle} ", ),
                html.Span(f"%{percentage}", )

            ], className=" m-auto space-x-4"),
            html.H1(value, className=f"m-auto text-3xl font-bold "),
            html.H2(title, className="text-2xl m-auto font-medium"),
            html.Span(sub_value, className="text-sm") if sub_value else None
        ],
        className=f"space-y-2 space-x-1 w-1/5  text-center flex-1  {style}"
    )
