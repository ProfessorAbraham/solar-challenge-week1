import pandas as pd
import streamlit as st
import plotly.express as px

def load_data():
    # Extract file IDs
    benin_id = "1D2yMBSSBIhNjSlmTstQF1rcL5owixA8_"
    sierra_id = "11VmH616dA_uCQGW3ie6QqgrFv-BXUrAD"
    togo_id = "1RjjKDc8yo9bHsktGWmrPCO5WPalSUgdF"

    # Convert to direct download links
    benin_url = f"https://drive.google.com/uc?id={benin_id}"
    sierra_url = f"https://drive.google.com/uc?id={sierra_id}"
    togo_url = f"https://drive.google.com/uc?id={togo_id}"

    benin = pd.read_csv(benin_url)
    sierra = pd.read_csv(sierra_url)
    togo = pd.read_csv(togo_url)

    benin['country'] = 'Benin'
    sierra['country'] = 'Sierra Leone'
    togo['country'] = 'Togo'

    return pd.concat([benin, sierra, togo], ignore_index=True)

def plot_box(data, feature):
    fig = px.box(data, x='country', y=feature, color='country', title=f'{feature} by Country')
    return fig

def top_region_table(data, feature, top_n=10):
    grouped = data.groupby('country')[feature].mean().reset_index()
    return grouped.sort_values(by=feature, ascending=False).head(top_n)
