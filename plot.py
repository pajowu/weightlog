import matplotlib.dates as md
import numpy as np
import matplotlib.pyplot as plt
from functions import *
import datetime
from scipy.interpolate import *
import math
def plot(weights, height=1.92, xkcd=False, target_bmi=None, long_dates=False, plot=True, save=False, outfile="out.png", show_bmi_steps=True):
    if xkcd:
        plt.xkcd()

    timestamps = [w['time'] for w in weights]
    weight_points = [w['weight'] for w in weights]

    dates=[datetime.datetime.fromtimestamp(ts) for ts in timestamps]

    ax=plt.gca()
    xfmt = md.DateFormatter('%d.%m.')
    ax.xaxis.set_major_formatter(xfmt)
    plt.scatter(dates,weight_points, zorder=2)

    x_sm = np.array(timestamps)
    y_sm = np.array(weight_points)

    seconds_diff = max(timestamps) - min(timestamps)
    num_steps = seconds_diff / 60 / 60 / 24 / 28 # one step every four weeks

    x_smooth = np.linspace(x_sm.min(), x_sm.max(), num_steps)
    y_smooth = interp1d(timestamps, weight_points, kind='linear')

    x_smooth_dates = [datetime.datetime.fromtimestamp(ts) for ts in x_smooth]
    plt.plot(x_smooth_dates, y_smooth(x_smooth), 'red', linewidth=1, zorder=1)

    if target_bmi:
        ax.add_line(plt.axhline(target_bmi*(height**2)))

    plt.axis('normal')

    ax.set_ylabel("Weight (kg)",fontsize=14,color='black')
    ax.set_xlabel('Time', fontsize=14, color='b')

    if show_bmi_steps:
        ax2 = ax.twinx()
        ax2.tick_params(which = 'both', direction = 'out')
        ax2.set_ylabel("BMI",fontsize=14,color='black')
        wmin, wmax = ax.get_ylim()
        bmin = wmin/(height**2)
        bmax = wmax/(height**2)
        ax2.set_ylim(ymin=bmin, ymax=bmax)
        step_size = 0.5
        st = math.ceil(bmin/step_size) * 0.5
        minor_ticks = np.arange(st, bmax, step_size)
        ax2.set_yticks(minor_ticks, minor=True)
        ax2.grid(which='minor', alpha=0.5)
        ax2.grid(which='major', alpha=0.75)


    if plot:
        plt.show()
    if save:
        plt.savefig(outfile, bbox_inches='tight')
    # close plot so we can draw multiple plots without reimportint pyplot
    plt.close()
