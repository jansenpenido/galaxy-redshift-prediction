# Galaxy Redshift Estimator
This application was developed as an exercise for Coursera's [Data-driven Astronomy](https://www.coursera.org/learn/data-driven-astronomy) course.


## Overview
To calculate the redshift of a distant galaxy, the most accurate method is to observe the optical emission lines and measure the shift in wavelength. However, this process can be time consuming and is thus infeasible for large samples.

For many galaxies we simply don't have spectroscopic observations. Instead, we can calculate the redshift by measuring the flux using a number of different filters and comparing this to models of what we expect galaxies to look like at different redshifts.

This Python program estimates the redshift of galaxies from the [Sloan Digital Sky Survey (SDSS)](http://www.sdss.org/). The data is stored as a [Numpy structured array](https://docs.scipy.org/doc/numpy/user/basics.rec.html).

To do so, it takes photometric readings of galaxies and calculates their corresponding colour indexes according to SDSS's filters received in five frequency bands (u, g, r, i and z). Each filter measures the light from the galaxy in a particular wavelength range.

Using the resulting colors, the redshift predictions are made using scikit-learn's `DecisionTreeRegressor` class.

![vega](http://www.astroml.org/_images/plot_sdss_filters_1.png)

*The five SDSS filter bands along with a spectrum of the star Vega. Source: [AstroML](http://www.astroml.org/examples/datasets/plot_sdss_filters.html)*


## Dependencies
* [Numpy](http://www.numpy.org/)
* [Sklearn](http://scikit-learn.org/stable/)
* [Matplotlib](https://matplotlib.org/)


## Author
[Jansen Penido](https://about.me/jansen.penido)
