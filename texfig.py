"""
Utility to generate PGF vector files from Python's Matplotlib plots to use in LaTeX documents.

Read more at https://github.com/knly/texfig
"""

import matplotlib as mpl
mpl.use('pgf')

from math import sqrt
default_width = 5.78853 # in inches
default_ratio = (sqrt(5.0) - 1.0) / 2.0 # golden mean
default_types = ['pdf', 'pgf']

mpl.rcParams.update({
    "text.usetex": True,
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
    "font.family": "serif",
    "font.serif": [],
    "font.sans-serif": [],
    "font.monospace": [],
    "figure.figsize": [default_width, default_width * default_ratio],
    "pgf.preamble": [
        # put LaTeX preamble declarations here
        r"\usepackage[utf8x]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{amsmath}",
        r"\usepackage{bm}",
        r"\usepackage{relsize}",
        r"\usepackage{calc}",
    ],
    "xtick.labelsize": "small",
})

import seaborn as sns
# font size 11pt
sns.set_context('paper', font_scale=10/12/0.8)
#sns.set_context('notebook', font_scale=11/12)
import matplotlib.pyplot as plt


"""
Returns a figure with an appropriate size and tight layout.
"""
def figure(width=default_width, ratio=default_ratio, tight_layout=False, pad=0, *args, **kwargs):
    fig = plt.figure(figsize=(width, width * ratio), *args, **kwargs)
    if tight_layout:
        fig.set_tight_layout({
            'pad': pad
        })
    return fig


"""
Returns subplots with an appropriate figure size and tight layout.
"""
def subplots(*args, width=default_width, ratio=default_ratio, tight_layout=False, **kwargs):
    fig, axes = plt.subplots(figsize=(width, width * ratio), *args, **kwargs)
    if tight_layout:
        fig.set_tight_layout({
            'pad': 0
        })
    return fig, axes


"""
Save both a PDF and a PGF file with the given filename.
"""
def savefig(filename, *args, **kwargs):
    for t in default_types:
        plt.savefig(filename + f'.{t}', *args, **kwargs)
