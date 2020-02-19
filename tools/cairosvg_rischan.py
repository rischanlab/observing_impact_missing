# Converst SVG to PDF recrusively 
from pathlib import Path
import cairosvg
import os

for filename in Path('figure_10_feb_2020').rglob('*.svg'):
	#print(filename)
	x = os.path.splitext(filename)[0]
	#print(x)
	cairosvg.svg2pdf(url= x + '.svg', write_to= x +'.pdf')


