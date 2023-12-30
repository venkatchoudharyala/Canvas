import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd

hide_st_style = """
                <style>
		.CanvasToolbar_enabled__2bOtL {display: none;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_st_style, unsafe_allow_html = True)

CheckPoint = 349
def MathFormulae():
	Formulae = pd.read_excel("MathData/Math_Equations.xlsx")
	return Formulae.values.tolist()
FormList = MathFormulae()

# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = 3
stroke_color = "#000000"
bg_color = "#eee"
realtime_update = False

st.latex(FormList[CheckPoint][0])
st.divider()

# Create a canvas component
canvas_result = st_canvas(
    fill_color = "rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width = stroke_width,
    stroke_color = stroke_color,
    background_color = bg_color,
    background_image = None,
    update_streamlit = realtime_update,
    height = 250, 
    width = 1000,
    drawing_mode=drawing_mode,
    point_display_radius = 0,
    key = "canvas",
)

# Image display
if canvas_result.image_data is not None and st.button("Review"):
    with st.container():
	    st.image(canvas_result.image_data)

