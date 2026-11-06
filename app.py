import plotly.express as px
import pandas as pd

# Même source de données que l'exemple du dépôt
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
données = pd.read_csv(URL)

# Exemple du dépôt (gardé) : quantité vendue par région
figure = px.pie(données, values='qte', names='region', title='Quantité vendue par région')
figure.write_html('ventes-par-region.html')

# Graphique 1 : ventes par produit (quantité vendue)
figure_ventes = px.pie(données, values='qte', names='produit', title='Quantité vendue par produit')
figure_ventes.write_html('ventes-par-produit.html')

# Graphique 2 : chiffre d'affaires par produit
données['chiffre_affaires'] = données['prix'] * données['qte']
ca_par_produit = données.groupby('produit', as_index=False)['chiffre_affaires'].sum()
figure_ca = px.bar(
    ca_par_produit,
    x='produit',
    y='chiffre_affaires',
    title="Chiffre d'affaires par produit",
    labels={'chiffre_affaires': "Chiffre d'affaires", 'produit': 'Produit'},
)
figure_ca.write_html('chiffre-affaires-par-produit.html')

print('Graphiques générés avec succès !')