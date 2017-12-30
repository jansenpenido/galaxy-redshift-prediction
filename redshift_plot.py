"""
SDSS Redshift - Plot
--------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":

    # Load SDSS redshift data
    data = np.load('data/sdss_galaxy_colors.npy')

    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define colour indexes u-g and r-i
    x = data['u'] - data['g']
    y = data['r'] - data['i']

    # Make a redshift array
    redshift = data['redshift']

    # Create the plot with plt.scatter and plt.colorbar
    plt.scatter(x, y, c=redshift, lw=0, s=5, cmap=cmap)
    cbar = plt.colorbar()

    # Get the axis reference
    axis = plt.gca()

    # Define axis labels and plot title
    plt.title('Redshift (colour) u-g versus r-i')

    cbar.set_label('Redshift')

    axis.set_xlabel('Colour index u-g')
    axis.set_ylabel('Colour index r-i')

    # Set axis limits
    axis.set_xlim([-0.5,2.5])
    axis.set_ylim([-0.5,1])

    plt.show()
