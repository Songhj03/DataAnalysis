import pandas as pd
import numpy as np

import plotly.figure_factory as ff
import plotly.offline as py 
import statistics
import plotly.express as px
import matplotlib.pyplot as plt


data = pd.read_csv('cox-violent-parsed_filt_usable.csv', usecols=['title', 'series', 'author', 'rating', 'language', 'genres', 'characters', 'pages', 'publishDate', 'awards', 'numRatings', 'likedPercent', 'price'])
data.head()