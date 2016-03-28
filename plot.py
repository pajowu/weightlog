
import numpy as np
import matplotlib.pyplot as plt
from functions import *
import datetime
from scipy.interpolate import *
import math
def plot(weights, height=1.92, xkcd=False, target_bmi=None, long_dates=False, plot=True, save=False, outfile="out.png"):
    if xkcd:
        plt.xkcd()
    time_points = [w['time'] for w in weights]
    weight_points = [w['weight'] for w in weights]
    x = time_points
    y = weight_points
    #f2 = interp1d(time_points, weight_points, kind='linear')
    f2 = PchipInterpolator(time_points, weight_points)
    #f2 = Akima1DInterpolator(time_points, weight_points)
    #f2 = UnivariateSpline(time_points, weight_points)
    xnew = np.linspace(min(time_points), max(time_points), 100)
    plt.plot(time_points,weight_points,'o',xnew, f2(xnew),'--')
    if long_dates:
        labels = [datetime.datetime.fromtimestamp(int(time)).strftime('%d.%m.%Y %H:%M') for time in time_points]
    else:
        labels = [datetime.datetime.fromtimestamp(int(time)).strftime('%d.%m.') for time in time_points]
    
    plt.xticks(time_points, labels, rotation=90)

    plt.scatter(x, y)
    ax = plt.gca()

    if target_bmi:
        ax.add_line(plt.axhline(target_bmi*(height**2)))
    ax2 = ax.twinx()
    ax2.tick_params(which = 'both', direction = 'out')
    
    plt.axis('normal')

    ax.set_ylabel("Weight (kg)",fontsize=14,color='blue')
    ax2.set_ylabel("BMI",fontsize=14,color='blue')
    
    wmin, wmax = ax.get_ylim()
    bmin = wmin/(height**2)
    bmax = wmax/(height**2)
    ax2.set_ylim(ymin=bmin, ymax=bmax)

    minor_ticks = np.arange(math.floor(bmin), bmax+1, .25)
    ax2.set_yticks(minor_ticks, minor=True)
    ax2.grid(which='minor', alpha=0.5) 

    ax.set_xlabel('Time', fontsize=14, color='b')
    if plot:
        plt.show()
    if save:
        plt.savefig(outfile)
