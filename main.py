import os
import glob

if __name__ == '__main__':
    print('debug point')
    from dashboards.homepage import layout
    from core import app

    app.layout = layout

    app.run_server(debug=True)
