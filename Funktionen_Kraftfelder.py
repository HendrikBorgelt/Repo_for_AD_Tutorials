import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd

import numpy
from stl import mesh
# fig.add_trace( ... )
# fig.update_layout( ... )
import pywavefront
import copy
import BasisFunktionen as bf


def create_mesh3d_for_vectorfeld(x_center,x_width, y_center, y_width, z_center, z_width, direction, scalefactor, linspace_dim, angle):
    a_234 = linspace_dim
    alpha_234 = angle*0.8
    x_234 = np.array(np.linspace(x_center - x_width,x_center + x_width,a_234).tolist()*a_234)
    y_234 = np.array((np.linspace(225+y_center,225+y_center,a_234) - np.linspace(225+y_center,225+y_center,a_234)*np.cos(np.linspace(-alpha_234/360*np.pi,alpha_234/360*np.pi,a_234))).tolist()*a_234)*-1 + np.linspace(y_center-(direction*5/a_234*scalefactor/x_width*20), y_center-(direction*5/a_234*scalefactor/x_width*20),a_234*a_234)
    z_234 = np.array(np.repeat(np.linspace(z_center - z_width, z_center + z_width, a_234).tolist(),a_234))
    # # u_234 = np.array(np.linspace(0,0,25))
    u_234 = direction*np.array(np.sin(np.linspace(-alpha_234/360*np.pi,alpha_234/360*np.pi,a_234)).tolist()*a_234)
    # # v_234 = np.array(np.linspace(1,1,25))
    v_234 = direction*np.array(np.cos(np.linspace(-alpha_234/360*np.pi,alpha_234/360*np.pi,a_234)).tolist()*a_234)
    w_234 = np.array(np.linspace(0,0,a_234*a_234))
    mesh_data = go.Cone(x=x_234, y=y_234, z=z_234,
                        u=u_234,  v=v_234, w=w_234,
                        opacity=0.8, sizemode="scaled", sizeref=5/a_234*scalefactor/ x_width * 20,
                        colorscale= [[0, 'gray'], [1, 'gray']], showscale=False, visible=False, hoverinfo='none')

    return mesh_data
