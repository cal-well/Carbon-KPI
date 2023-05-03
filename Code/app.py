import streamlit as st

"## Create a 3D map using Kepler.gl"

import streamlit as st
import leafmap.kepler as leafmap

m = leafmap.Map()
in_csv = 'https://raw.githubusercontent.com/cal-well/Carbon-KPI/main/Data/Housing%20Data.csv'
config = 'https://raw.githubusercontent.com/cal-well/Carbon-KPI/main/Data/config.json'
m.add_csv(in_csv, layer_name="Housing Data", config=config)
m.to_streamlit()