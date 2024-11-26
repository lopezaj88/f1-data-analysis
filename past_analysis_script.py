# -*- coding: utf-8 -*-

"""
past_analysis_script.py- Analyzes the performance of drivers at a specified circuit.  
"""

__author__ = "Austin Lopez"
__version__ = "1.5"
__email__ = "formulas.for.f1@gmail.com"
__status__ = "Production"

# Import Modules
import fastf1 as ff1
import fastf1.plotting as f1plot
from matplotlib import pyplot as plt

# Define variables
year = 2023
location = 'Qatar'
ses = 'R'
mclaren = ['NOR', 'PIA']
ferrari = ['SAI', 'LEC']
redBull = ['VER', 'PER']
mercedes = ['HAM', 'RUS']
astonMartin = ['ALO', 'STR']
haas = ['HUL', 'MAG']
alpine = ['GAS', 'OCO']
vcarb = ['TSU']
williams = ['ALB']
sauber = ['BOT', 'ZHO']
teams = [mclaren, ferrari, redBull, mercedes, astonMartin, haas, alpine, vcarb, williams, sauber]
cache = 'Cache_Qatar_2023'

# Enable Cache and set up plotting
#ff1.Cache.enable_cache(cache)
f1plot.setup_mpl(color_scheme='fastf1', misc_mpl_mods=False)

# Load session data
race = ff1.get_session(year, location, ses)
race.load()
