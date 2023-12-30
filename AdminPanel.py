import streamlit as st
import json
import os
import pandas as pd
import base64
import io
from PIL import Image

st.set_page_config(initial_sidebar_state = "collapsed")

hide_st_style = """
		<style>
		header {visibility: hidden;}
		footer {visibility: hidden;}
  		</style>
  		"""

st.markdown(hide_st_style, unsafe_allow_html = True)

def Scrapper():
	Form = st.form("Login")
	dir = os.listdir("UserAcc")
	MPath = st.selectbox("Users", dir)
	#UserName = Form.text_input("User Name")
	Path = "UserAcc/" + MPath
	Rapo(Path)
def Rapo(Path):
	try:
		with open(Path, "r") as File:
			UDetails = File.read()
			Details = json.loads(UDetails)
			st.write(Details)
			DisplayImage(Details["FilePath"])
	except FileNotFoundError:
		st.write("User Not Found")

def DisplayImage(path):
	df = pd.read_excel(path)
	st.dataframe(df)
	
	for index, row in df.iterrows():
		text = row["FORMULA_IN_LATEX"]
		image_bytes = bytes(row["IMAGE_DATA_IN_PNG"], encoding = 'utf-8')
		#image_io = io.BytesIO(imag_bytes)
		#pil_imager = Image.open(image_io)
		#st.write(text)
		st.image(image_bytes)
