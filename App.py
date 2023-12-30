import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd

hide_st_style = """
                <style>
                header {visibility: hidden;}
                footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_st_style, unsafe_allow_html = True)

CheckPoint = 89
def MathFormulae():
	Formulae = pd.read_excel("MathData/Math_Equations.xlsx")
	return Formulae.values.tolist()
FormList = MathFormulae()

# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = 3
stroke_color = "#000000"
bg_color = "#eee"
realtime_update = True

#Exported_Latex_Code = "a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)"
#Display_Latex_Code = "r'''" + Exported_Latex_Code + "'''"
#st.latex(Display_Latex_Code)
#st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')
st.latex(FormList[CheckPoint][0])

# Create a canvas component
canvas_result = st_canvas(
    fill_color = "rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width = stroke_width,
    stroke_color = stroke_color,
    background_color = bg_color,
    background_image = None,
    update_streamlit = realtime_update,
    height = 150, 
    width = 500,
    drawing_mode=drawing_mode,
    point_display_radius = 0,
    key = "canvas",
)

# Image display
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)

