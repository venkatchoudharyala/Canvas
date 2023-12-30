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

CheckPoint = 99
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
    height = 500, 
    width = 1000,
    drawing_mode=drawing_mode,
    point_display_radius = 0,
    key = "canvas",
)

# Image display
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
def enter_fullscreen():
    try:
        # Try the current method
        st.markdown("""
        <script>
        document.documentElement.requestFullscreen();
        </script>
        """, unsafe_allow_html=True)
    except:
        # Fallback to alternative method if requestFullscreen fails
        st.markdown("""
        <script>
        if (window.screenTop && window.screenTop.window) {
            window.screenTop.window.document.documentElement.requestFullscreen();
        } else {
            window.document.documentElement.requestFullscreen();
        }
        </script>
        """, unsafe_allow_html=True)

# Button to trigger full-screen
if st.button("Enter Full Screen"):
    enter_fullscreen()

