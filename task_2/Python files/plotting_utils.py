import pyvista as pv
import matplotlib.pyplot as plt


def plot_frame(plotter, frame):
    """
    Plots the given frame using PyVista.    
    """
    # Origin of the frame
    origin = frame[:3, 3]

    x_axis = frame[:3, 0]
    
    y_axis = frame[:3, 1]

    z_axis = frame[:3, 2]
    
    # Plot the three axes
    plotter.add_arrows(cent=origin, direction=x_axis, color="red")
    plotter.add_arrows(cent=origin, direction=y_axis, color="green")
    plotter.add_arrows(cent=origin, direction=z_axis, color="blue")


def plot_color(plotter, points, colors):
    """
    Plots a 3D color projection of points using PyVista.

    Parameters:
    points (numpy.ndarray): (D, N), only first 3 dimensions of D are plotted
    colors (numpy.ndarray): (3, N), where each column is an RGB color [R, G, B].

    Returns:
    None
    """
    points = points.T
    cloud = pv.PolyData(points[:, :3])
    cloud["colors"] = colors.T

    plotter.add_points(cloud, scalars="colors", rgb=True, point_size=2)


def plot_color_projection(points, colors):
    """
    Plots a 2D color projection using matplotlib.

    Parameters:
    points (numpy.ndarray): (D, N), only first 2 dimensions of D are plotted
    colors (numpy.ndarray): (3, N), where each column is an RGB color [R, G, B].

    Returns:
    None
    """
    points = points.T
    colors = colors.T
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Extract x and y coordinates
    x, y = points[:, 0], points[:, 1]

    # Create scatter plot
    ax.scatter(x, y, c=colors, s=2)

    # Set equal aspect ratio
    ax.set_aspect("equal")

    ax.invert_yaxis()
    ax.set_axis_off()
