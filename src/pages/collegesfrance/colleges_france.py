from dash import  html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import pandas as pd

register_page(__name__, icon="dashicons:admin-multisite")
# CSS
center ={'text-align' : 'center'}
center_ojbect = {"margin-left": "auto", "margin-right": "auto"}
center_title = {'text-align' : 'center', "margin-top" : "30px", "margin-bottom" : "30px"}

# LOAD DATA

urlnat = "https://filedn.eu/lHdttuiSAwVYBLWzET7NL14/DATASETS/colleges_fr.csv"
dfnat = pd.read_csv(urlnat)


# variables nationales :
totalnat = dfnat['nombre_deleves_total'].sum()
default_public = round(dfnat[dfnat['secteur_PUBLIC'] > 0]['nombre_deleves_total'].sum()/dfnat['nombre_deleves_total'].sum()*100,1)
default_prive = round(dfnat[dfnat['secteur_PRIVE'] > 0]['nombre_deleves_total'].sum()/dfnat['nombre_deleves_total'].sum()*100,1)



# OPTION zonage:
zone_option = [{"label": f"Département : {x}", "value": x} for x in dfnat.sort_values(by='departement')['departement'].unique()]


layout = html.Div(
    [

# national :
        dmc.Title("Synthèse Nationale (France Métropolitaine)", order=1, style=center_title),
        dmc.Grid(
            children=[
                        dmc.Col(
                    [
                            dmc.Card(
                                children=[
                                            dmc.Text("Nombre d'élèves en collège :",style=center),
                                            dmc.Badge(f"{totalnat:,} élèves".replace(',', ' '),style=center, variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, size ="lg", fullWidth=True),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                style={"width": "auto", "height": "auto", "margin": "auto"},
                            )
                    ]

                    , span=3),
                            dmc.Col(
                    [
                            dmc.Card(
                                children=[
                                            dmc.Text("Nombre de collèges :",style=center),
                                            dmc.Badge(f"{dfnat['departement'].count()} collèges",style=center, variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, size ="lg", fullWidth=True),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                style={"width": "auto", "height": "auto", "margin": "auto"},
                            )
                    ]

                    , span=3),
                        dmc.Col(
                    [
                            dmc.Card(
                                children=[
                                            dmc.Text("Pourcentage de collèges publics :",style=center),
                                            dmc.Badge(f"{round(dfnat['secteur_PUBLIC'].sum()/dfnat.shape[0]*100,1)} %",style=center, variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, size ="lg", fullWidth=True),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                style={"width": "auto", "height": "auto", "margin": "auto"},
                            )
                    ]

                    , span=3),
                            dmc.Col(
                    [
                            dmc.Card(
                                children=[
                                            dmc.Text("Pourcentage de collèges privés :",style=center),
                                            dmc.Badge(f"{round(dfnat['secteur_PRIVE'].sum()/dfnat.shape[0]*100,1)} %",style=center, variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, size ="lg", fullWidth=True),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                style={"width": "auto", "height": "auto", "margin": "auto"},
                            )
                    ]

                    , span=3),
            ],
            gutter="xl",
        ),


# -----------------------------------------------------------------------------------------------------------------------------------------------------------DEPARTEMENTS :
        dmc.Title("Synthèse Départementale", order=1, style=center_title),
        dmc.Select(
            id="dropdown",
            data=zone_option,
            value='GIRONDE',
            clearable=False,
        style={"padding-bottom": "10px"}),
        dmc.Grid(
            children=[
                dmc.Col(
                    [
                            dmc.Card(
                                children=[
                                            dmc.Text("Nombre d'élèves :", weight=500, style=center),
                                            dmc.Badge(id="total_eleves", variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, size ="lg", fullWidth=True),
                                ],
                                withBorder=True,
                                shadow="sm",
                                radius="md",
                                style={"width": "auto", "margin": "auto"},
                            )
                    ]

                    , span=3),
                dmc.Col([
                    dmc.Card(
                        children=[
                            dmc.Text("Ratio échelle Nationale", weight=500, style=center),
                            dmc.Badge(id="ratio_national", variant="gradient",
                                      gradient={"from": "teal", "to": "lime", "deg": 105}, size="lg", fullWidth=True),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": "auto", "margin": "auto"},
                    )



                ], span=3),
                dmc.Col([
                    dmc.Card(
                        children=[
                            dmc.Text("Nombre d'élèves en Segpa", weight=500, style=center),
                            dmc.Badge(id="nb_segpa", variant="gradient",
                                      gradient={"from": "teal", "to": "lime", "deg": 105}, size="lg", fullWidth=True),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": "auto", "margin": "auto"},
                    )

                ], span=3),
                dmc.Col([
                    dmc.Card(
                        children=[
                            dmc.Text("Nombre d'élèves en Ulis", weight=500, style=center),
                            dmc.Badge(id="nb_ulis", variant="gradient",
                                      gradient={"from": "teal", "to": "lime", "deg": 105}, size="lg", fullWidth=True),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": "auto", "margin": "auto"},
                    )

                ], span=3),
            ],
            gutter="xl"
        ),
#------------------------------------------------------------------------deuxième ligne :
        dmc.Grid(children=[
                            dmc.Col(
                            [
                                dmc.Card(children=[
                                    dmc.Text("Elèves dans le secteur public :"),
                                    dmc.RingProgress(
                                            sections=[{"value": 33, "color": "green"}],
                                            label=dmc.Center(dmc.Text(id="ring_public", color="green")),
                                        ),])
                                    ]

                                    , span=3),
                            dmc.Col(
                            [
                                dmc.Card(children=[
                                    dmc.Text("Elèves dans le secteur privé :"),
                                    dmc.RingProgress(
                                            sections=[{"value": 33, "color": "green"}],
                                            label=dmc.Center(dmc.Text(id="ring_prive", color="green")),
                                        ),])
                                    ]

                                    , span=3),



                ],gutter="xl")
    ]
)

@callback([
    Output("total_eleves", "children"),
    Output('ratio_national', 'children'),
    Output('nb_segpa', 'children'),
    Output('nb_ulis', 'children'),
    Output('ring_public', 'children'),
    Output('ring_prive', 'children'),
                ],
          [Input("dropdown", "value")]
)
def update_values(departement):

    urlnat = "https://filedn.eu/lHdttuiSAwVYBLWzET7NL14/DATASETS/colleges_fr.csv"
    dfnat = pd.read_csv(urlnat)

    df = dfnat[dfnat['departement'] == departement]
    df_filtre = dfnat[dfnat['departement'] == departement]


    total_eleves = df_filtre['nombre_deleves_total'].sum()
    result_total_eleves = f"{str(total_eleves)[:-3]},{str(total_eleves)[-2:]}K"
    ratio_national = f"{round((df_filtre.nombre_deleves_total.sum()/dfnat['nombre_deleves_total'].sum())*100, 1)} %"
    nb_segpa = f"{df_filtre['nombre_deleves_total_segpa'].sum():,}".replace(',', ' ')
    nb_ulis = f"{df_filtre['nombre_deleves_total_ulis'].sum():,}".replace(',', ' ')
    ring_public = f"{round(df_filtre[df_filtre['secteur_PUBLIC'] > 0]['nombre_deleves_total'].sum()/df_filtre['nombre_deleves_total'].sum()*100,1)} %"
    ring_prive = f"{round(df_filtre[df_filtre['secteur_PRIVE'] > 0]['nombre_deleves_total'].sum()/df_filtre['nombre_deleves_total'].sum()*100,1)} %"

    return  result_total_eleves, ratio_national, nb_segpa, nb_ulis,ring_public, ring_prive