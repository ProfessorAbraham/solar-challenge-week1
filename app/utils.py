import pandas as pd
import os
import streamlit as st
import plotly.express as px

def load_data():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    benin = pd.read_csv(os.path.join(base_path, 'eda-benin.csv'))
    sierra = pd.read_csv(os.path.join(base_path, 'sierra_leone.csv'))
    togo = pd.read_csv(os.path.join(base_path, 'eda-togo.csv'))

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
