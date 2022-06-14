from dash import html


def Box(children: list = None, title: str = None) -> html:
    return html.Div([
        html.Div(
            html.H1(title, className="font-bold text-2xl", style={"color": "darkblue"})
        ),
        html.Hr(className="text-gray w-full"),
        html.Div(children)
    ], className="w-full h-auto rounded-xl py-2 px-4 hover:border-red", style={"backgroundColor": "aliceblue"})
