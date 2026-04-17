import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load datasets
abnb = pd.read_csv("ABNB.csv")
tsa = pd.read_csv("tsa_passenger_volumes.csv")
cpi = pd.read_csv("fred_cpi_lodging_away_from_home.csv")

# Print to check
print("ABNB:")
print(abnb.head())

print("\nTSA:")
print(tsa.head())

print("\nCPI:")
print(cpi.head())
