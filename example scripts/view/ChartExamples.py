"""
Chart Examples in matplotlib
This set of examples comes from https://www.python-course.eu/matplotlib_overview.php
Recommend you read that webpage.

To use matplotlib.pyploy, import it. 
If it is not installed you will need to install it into your python globally or virtual environment. 
See here: https://www.tutorialspoint.com/how-to-install-matplotlib-in-python

To use numpy import it.
If it is not installed you will need to install it into your python globally or virtual environment. 
See here: https://numpy.org/install/ (recommend you use "pip")

Documentation
A summary of matlibplot.pyplot 
See here: https://matplotlib.org/stable/api/pyplot_summary.html

Details of matlibplot.pyplot.plot.
See here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

"""


import sys
sys.dont_write_bytecode = True

import matplotlib.pyplot as plt
import numpy as np

def line_plot(**kwargs):
    """
    Automagically takes a list of Y values (data) and figures out the X axis.
    As a continuous graph.

    Args 
          **kwargs lets you pass arguments into this function 
    """
    data_values = [-1, -4.5, 16, 23]
    if 'data' in kwargs:
        data_values = kwargs['data']
    plt.plot(data_values)
     
    #plt.show()
    return plt.gcf()

def discrete_plot(**kwargs):
    """
    Plot format, sets marker in place of a continuous line. 

    Args 
          **kwargs lets you pass arguments into this function
    """
    data_values = [-1, -4.5, 16, 23]
    if 'data' in kwargs:
        data_values = kwargs['data']
    plt.plot(data_values, "ob")
    # See formating here :
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

    #plt.show()
    return plt.gcf()

def names_labels(**kwargs):
    """
    Use subplots() to plot with our own axies, for a figure.
        See here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot
        Set axies labels as kwargs in here:
        https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html

    This gets an Axes object

    X axis(days), Y axis (celsius_values)

    Args 
          **kwargs lets you pass arguments into this function
    """
    x_label = 'Day'
    y_label = 'Temperature in Celsius'
    title_label = 'Temperature Graph'
    x_values = range(1, 9)
    y_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    if 'x_label' in kwargs :
        x_label = kwargs['x_label']
    if 'y_label' in kwargs :
        y_label = kwargs['y_label']
    if 'title_label' in kwargs :
        title_label = kwargs['title_label']
    if 'x_values' in kwargs :
        x_values = kwargs['x_values']
    if 'y_values' in kwargs :
        y_values = kwargs['y_values']


    fig, ax = plt.subplots() # Challenge - Why "fig" here"

    ax.plot(x_values, y_values)
    ax.set(xlabel=x_label,
        ylabel=y_label,
        title=title_label)
    # See kwargs here https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html

    #plt.show()
    return plt.gcf()

def multiple_plots(**kwargs):
    """
    Plot more than one on a single graph
    Args 
          **kwargs lets you pass arguments into this function
    """
    days = list(range(1, 9))
    celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]

    fig, ax = plt.subplots()

    ax.set(xlabel='Day',
        ylabel='Temperature in Celsius',
        title='Temperature Graph')

    ax.plot(days, celsius_min)
    ax.plot(days, celsius_min, "oy")
    ax.plot(days, celsius_max)
    ax.plot(days, celsius_max, "or")

    # Short hand version in one call to plot
    # ax.plot(days, celsius_min,
    #   days, celsius_min, "oy",
    #   days, celsius_max,
    #   days, celsius_max, "or")
    return plt.gcf()

def bar_chart(**kwargs):
    """
    An example of a bar chart

    Args 
          **kwargs lets you pass arguments into this function
    """
    years = [str(year) for year in range(2010, 2021)]
    visitors = [1241, 50927, 162242, 222093, 
                665004, 2071987, 2460407, 3799215, 
                5399000, 5474016, 6003672]


    plt.bar(years, visitors, color="green")

    plt.xlabel("Years")
    plt.ylabel("Values")
    plt.title("Bar Chart Example")

    plt.plot()
     
    return plt.gcf()

def histogram(**kwargs):
    """
    An example of a histogram
    Uses numpy as np to get a list of values in a random range - Gaussian

    Args 
          **kwargs lets you pass arguments into this function

          This includes an example of how to change the plt 'title' by looking for it in **kwargs.
    """
    if kwargs['title']:
           plt.title(kwargs['title'])
    else:
           plt.title("Gaussian Histogram")

    gaussian_numbers = np.random.normal(size=10000)
    
    plt.hist(gaussian_numbers, bins=20)
    
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    #plt.show()
    return plt.gcf()

def scatter_plots(**kwargs):
    """
    Three Scatter plots over a range.
    Uses numpy as np.

    Args 
          **kwargs lets you pass arguments into this function
    """
    x = np.arange(0, 11)

    y1 = np.random.randint(2, 7, (11,))
    y2 = np.random.randint(9, 14, (11,))
    y3 = np.random.randint(15, 25, (11,))

    # Markers: https://matplotlib.org/api/markers_api.html

    plt.scatter(x, y1)
    plt.scatter(x, y2, marker='v', color='r')
    plt.scatter(x, y3, marker='^', color='m')
    plt.title('Scatter Plot Example')
    #plt.show()
    return plt.gcf()

def stack_plot(**kwargs):
    """
    Stack plot with three lists of values.

    Args 
          **kwargs lets you pass arguments into this function   
    """
    idxes = [ 1,  2,  3,  4,  5,  6,  7,  8,  9]
    y1  = [23, 42, 33, 43,  8, 44, 43, 18, 21]
    y2  = [9, 31, 25, 14, 17, 17, 42, 22, 28]
    y3  = [18, 29, 19, 22, 18, 16, 13, 32, 21]


    plt.stackplot(idxes, y1, y2, y3)
    plt.title('Stack Plot Example')

    #plt.show()
    return plt.gcf()

def pie_chart1(**kwargs):
    """
    Pie chart, where the slices will be ordered and plotted counter-clockwise.

    Args 
          **kwargs lets you pass arguments into this function
    """
    labels = 'C', 'Python', 'Java', 'C++', 'C#'
    sizes = [13.38, 11.87, 11.74, 7.81, 4.41]
    explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Python')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('TIOBE Index for May 2021')
    #plt.show()
    return plt.gcf()

def pie_chart2(**kwargs):
    """
    Another Pie Chart
    Pie chart, where the slices will be ordered and plotted counter-clockwise.

    Args 
          **kwargs lets you pass arguments into this function
    """
    labels = 'C', 'Python', 'Java', 'C++', 'C#', 'others'
    sizes = [13.38, 11.87, 11.74, 7.81, 4.41]
    sizes.append(100 - sum(sizes)) # << THIS IS THE "others". "sum(sizes)"" adds up all the items in the tuple?
    explode = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Python')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('TIOBE Index for May 2021')
    #plt.show()
    return plt.gcf()

def show_figFunc(pFigureFunction, **kwargs):
    """
    Shows a figure

    args
        pFigureFunction (a function that returns a matplotlib figure)\n
        **kwargs needs to match kwargs of the function
    """
    current_fig = fig_with_kwargs(pFigureFunction,**kwargs)
    plt.figure(current_fig.number)
    plt.show()

def fig_with_kwargs(pFigureFunction, **kwargs):
    """
    Returns a figure after appying the kwargs

    args
        pFigureFunction (a function that returns a matplotlib figure) \n
        **kwargs needs to match kwargs of the function
    """
    kwarg_fig = None
    if kwargs :
        kwarg_fig = pFigureFunction(**kwargs)
    else:
        kwarg_fig = pFigureFunction()

    return kwarg_fig

if __name__ == "__main__":
    # Test scripts
    show_figFunc(line_plot)

    show_figFunc(discrete_plot)

    show_figFunc(names_labels)

    show_figFunc(multiple_plots)
    show_figFunc(bar_chart)
    show_figFunc(histogram, title="Our Name for Title")
    show_figFunc(scatter_plots)
    show_figFunc(stack_plot)
    show_figFunc(pie_chart1)
    show_figFunc(pie_chart2)
    pass
