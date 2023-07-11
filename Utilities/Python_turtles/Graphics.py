from sketchpy import canvas
from sketchpy import library
import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm

def testsketch():
    obj = canvas.sketch_from_svg("Utilities/Python_turtles/harish.svg")
    obj.draw()
