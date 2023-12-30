import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pandas as pd
import io
import base64
from LoginApp import Page
import AdminPanel as ap

hide_st_style = """
                <style>
                header {visibility: hidden;}
                footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_st_style, unsafe_allow_html = True)

Page.main()

if "user" in st.session_state:
	UserDetails = st.session_state["user"]
	st.write(UserDetails)
	st.session_state["LoginVal"] = True
else:
	st.session_state["LoginVal"] = False

UserName = UserDetails["Name"]

def MathFormulae():
	Formulae = pd.read_excel("MathData/Math_Equations.xlsx")
	return Formulae.values.tolist()
FormList = MathFormulae()

CheckPoint = 349

def main():
	if UserName == "Admin":
		ap.Scrapper()
	else:
		# Specify canvas parameters in application
		drawing_mode = "freedraw"
		stroke_width = 3
		stroke_color = "#000000"
		bg_color = "#eee"
		realtime_update = True
		
		FormulaSpace = st.empty()
		def FormulaUpdater(CheckPoint):
			FormulaSpace.latex(FormList[CheckPoint][0])
		FormulaUpdater(CheckPoint)
		st.divider()
		
		# Create a canvas component
		canvas_result = st_canvas(
		    fill_color = "rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
		    stroke_width = stroke_width,
		    stroke_color = stroke_color,
		    background_color = bg_color,
		    background_image = None,
		    update_streamlit = realtime_update,
		    height = 150, 
		    width = 1000,
		    drawing_mode = drawing_mode,
		    point_display_radius = 0,
		    key = "canvas",
		)
		
		# Image display
		if canvas_result.image_data is not None:
			st.image(canvas_result.image_data)
			if st.button("Save and Proceed"):
				pil_image = Image.fromarray(canvas_result.image_data)
				image_bytes = io.BytesIO()
				pil_image.save(image_bytes, format="PNG")
				
				df = pd.read_excel("Files/DrawnImages.xlsx")
				df.loc[len(df.index)] = {"FORMULA_IN_LATEX": FormList[CheckPoint][0], "IMAGE_DATA_IN_PNG": image_bytes.getvalue()}
				df.to_excel("Files/DrawnImages.xlsx", index=False)
		
				CheckPoint += 1
				FormulaUpdater(CheckPoint)
				#st.experimental_rerun()
				#st.dataframe(df)

def DisplayImage():
	#DisplayImage(df["IMAGE_DATA_IN_PNG"][0])
	df = pd.read_excel("Files/DrawnImages.xlsx")
	print(df)
	
	for index, row in df.iterrows():
		text = row["FORMULA_IN_LATEX"]
		image_base64 = row["IMAGE_DATA_IN_PNG"]
		image_bytess = base64.b64decode(image_base64)
		image_io = io.BytesIO(image_bytess)
		pil_imager = Image.open(image_io)
		st.write(text)
		st.image(pil_imager)

if st.button("Show"):
	DisplayImage()

if __name__ == "__main()__":
	main()

