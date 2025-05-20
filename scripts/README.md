# Solar Dashboard (Streamlit)

## Description

This dashboard provides interactive visualizations for comparing solar energy metrics (e.g., GHI, DNI, DHI) across three West African countries: Benin, Sierra Leone, and Togo.

## Usage Instructions

1. Ensure you have the cleaned CSVs in a local `data/` folder:

   - data/eda-benin.csv
   - data/sierra_leone.csv
   - data/eda-togo.csv

2. Install required dependencies:

```bash
pip install streamlit pandas plotly
```

3. Run the dashboard locally:

```bash
streamlit run app/main.py
```

4. Use the sidebar to select countries and variables to visualize.

## Deployment

To deploy this app on Streamlit Community Cloud:

- Push this repo to GitHub.
- Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and connect your repo.
- Ensure your `data/` folder is included via `.streamlit/secrets.toml` or a cloud-accessible source if needed.

"""
