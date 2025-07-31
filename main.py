import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import numpy as np

x_vals = np.random.normal(loc=50, scale=15, size=200)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Needed for Replit

# Custom CSS for enhanced styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            @keyframes pulse {
                0%, 100% { opacity: 0.4; transform: scale(1); }
                50% { opacity: 1; transform: scale(1.2); }
            }
            
            .navbar-brand {
                font-weight: 600;
                letter-spacing: 0.5px;
            }
            
            .display-4 {
                line-height: 1.2;
            }
            
            .btn {
                font-weight: 500;
                letter-spacing: 0.5px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,123,255,0.2);
                transition: all 0.3s ease;
            }
            
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,123,255,0.3);
            }
            
            .btn-outline-primary:hover {
                box-shadow: 0 4px 12px rgba(0,123,255,0.2);
            }
            
            body {
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            }
            
            .logo-placeholder {
                width: 45px;
                height: 45px;
                background: linear-gradient(135deg, #007BFF, #17A2B8);
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: 700;
                font-size: 20px;
                box-shadow: 0 2px 8px rgba(0,123,255,0.2);
            }
            
            .brand-text {
                font-size: 1.4rem;
                font-weight: 600;
                color: #343a40;
                letter-spacing: 0.5px;
            }
            
            .btn-link {
                text-decoration: none !important;
                border: none;
                padding: 0.5rem 1rem;
                border-radius: 6px;
                transition: all 0.2s ease;
            }
            
            .btn-link:hover {
                background-color: rgba(0,123,255,0.05);
                transform: translateY(-1px);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

app.layout = dbc.Container(fluid=True, children=[
    # Custom Header with centered logo
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Button("Servicios", color="link", className="text-primary fw-semibold"),
                dbc.Button("Metodología", color="link", className="text-primary fw-semibold"),
            ], width=3, className="d-flex justify-content-end align-items-center gap-3"),
            
            dbc.Col([
                html.Div([
                    html.Div("M", className="logo-placeholder"),
                    html.Span("Marvento Analytics", className="brand-text")
                ], className="d-flex align-items-center justify-content-center gap-2")
            ], width=6, className="text-center"),
            
            dbc.Col([
                dbc.Button("Casos de Estudio", color="link", className="text-primary fw-semibold"),
                dbc.Button("Contacto", color="link", className="text-primary fw-semibold"),
            ], width=3, className="d-flex justify-content-start align-items-center gap-3"),
        ], className="align-items-center py-3")
    ], fluid=True, className="border-bottom border-light"),

    # Hero Section
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1([
                    "Consultoría en ", 
                    html.Span("Estadística", className="text-primary fw-bold"),
                    " e ",
                    html.Span("Inteligencia Artificial", className="text-info fw-bold")
                ], className="display-4 fw-light mb-4"),
                
                html.P([
                    "Transformamos datos complejos en decisiones estratégicas mediante modelos estadísticos avanzados ",
                    "y algoritmos de inteligencia artificial de última generación."
                ], className="lead mb-4 text-muted", style={"max-width": "650px", "margin": "0 auto"}),
                
                html.Div([
                    dbc.Button("Iniciar Proyecto", color="primary", size="lg", className="me-3 px-4 py-2"),
                    dbc.Button("Ver Casos de Estudio", color="outline-primary", size="lg", className="px-4 py-2")
                ], className="d-flex justify-content-center gap-3 mb-5"),
                
                # Subtle data visualization accent
                html.Div([
                    html.Div(className="hero-dot", style={
                        "width": "8px", "height": "8px", "background": "#007BFF", 
                        "border-radius": "50%", "display": "inline-block", "margin": "0 4px",
                        "animation": "pulse 2s infinite"
                    }),
                    html.Div(className="hero-dot", style={
                        "width": "12px", "height": "12px", "background": "#17A2B8", 
                        "border-radius": "50%", "display": "inline-block", "margin": "0 4px",
                        "animation": "pulse 2s infinite 0.5s"
                    }),
                    html.Div(className="hero-dot", style={
                        "width": "6px", "height": "6px", "background": "#6C757D", 
                        "border-radius": "50%", "display": "inline-block", "margin": "0 4px",
                        "animation": "pulse 2s infinite 1s"
                    }),
                    html.Div(className="hero-dot", style={
                        "width": "10px", "height": "10px", "background": "#007BFF", 
                        "border-radius": "50%", "display": "inline-block", "margin": "0 4px",
                        "animation": "pulse 2s infinite 1.5s"
                    }),
                ], className="text-center")
                
            ], className="text-center py-5", style={
                "background": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
                "border-radius": "20px",
                "margin": "2rem 0"
            })
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            html.H3("Análisis de Distribución de Clientes"),
            dcc.Slider(
                id='bin-slider',
                min=5, max=50, step=1, value=20,
                marks={i: str(i) for i in range(5, 51, 5)},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            dcc.Graph(id="histogram")
        ])
    ], className="mt-4"),

    dbc.Row([
        dbc.Col([
            html.H4("Contacto"),
            html.P("📬 contacto@marvento.com"),
        ])
    ], className="mt-5 mb-5")
])

@app.callback(
    Output("histogram", "figure"),
    Input("bin-slider", "value")
)
def update_histogram(bins):
    fig = go.Figure([
        go.Histogram(x=x_vals, nbinsx=bins, marker_color="#007BFF")
    ])
    fig.update_layout(margin=dict(l=10, r=10, t=30, b=40))
    return fig

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
