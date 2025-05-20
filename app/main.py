import streamlit as st
from utils import load_data, plot_box, top_region_table


st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("🌞 West Africa Solar Data Dashboard")

# Load data
data = load_data()

# Sidebar widgets
st.sidebar.header("Filter Options")
country_options = data['country'].unique().tolist()
selected_countries = st.sidebar.multiselect("Select Countries:", options=country_options, default=country_options)

plot_feature = st.sidebar.selectbox("Select Feature to Plot (Boxplot):", ["GHI", "DNI", "DHI", "ModA", "ModB", "Tamb", "WS"])
top_feature = st.sidebar.selectbox("Select Feature for Top Regions Table:", ["GHI", "DNI", "DHI", "ModA", "ModB", "Tamb", "WS"])

filtered_data = data[data['country'].isin(selected_countries)]

# Boxplot
st.subheader(f"📊 Boxplot of {plot_feature}")
st.plotly_chart(plot_box(filtered_data, plot_feature), use_container_width=True)

# Top regions table
st.subheader(f"🏆 Average {top_feature} by Country")
st.dataframe(top_region_table(filtered_data, top_feature))