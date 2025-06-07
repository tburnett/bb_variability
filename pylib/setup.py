import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def set_theme(argv):
    plt.rcParams['figure.figsize']=[6,5]
    # sns.set_theme('notebook' if 'talk' not in argv else 'talk', font_scale=1.25) 
    sns.set_theme( 'talk', font_scale=1.) 
    if 'paper' in argv: 
        # sns.set_theme('paper')
        sns.set_style('ticks')
    if 'dark' in argv:
        sns.set_style('darkgrid') ##?
        plt.style.use('dark_background')
        plt.rcParams['grid.color']='0.5'
        plt.rcParams['figure.facecolor']='k'
        dark_mode=True
    else:
        dark_mode=False
        sns.set_style('ticks' if 'paper' in argv else 'whitegrid')
        plt.rcParams['figure.facecolor']='white'
    return dark_mode

set_theme(sys.argv)