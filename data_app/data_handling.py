from dash import html
import io
import base64
import pandas as pd

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif ('xls' | 'xlsx') in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        elif 'json' in filename:
            df = pd.read_json(io.StringIO(decoded.decode('utf-8')))
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])
    
    return df