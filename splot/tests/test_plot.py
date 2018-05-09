import matplotlib.pyplot as plt
import pysal as ps
from libpysal.api import queen_from_shapefile
from esda.moran import Moran
from pysal.contrib.pdio import read_files

from splot.plot import mplot


def test_mplot():
    link = ps.examples.get_path('columbus.shp')

    db = read_files(link)
    y = db['HOVAL'].values
    w = queen_from_shapefile(link)
    w.transform = 'R'

    m = Moran(y, w)

    fig = mplot(m, xlabel='Response', ylabel='Spatial Lag',
                title='Moran Scatterplot', custom=(7,7))
    plt.close(fig)
