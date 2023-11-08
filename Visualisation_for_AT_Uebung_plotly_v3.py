# import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from stl import mesh

import Funktionen_Differentielles_Element as fd
import Funktionen_Pfeil as fp
import Funktionen_Moment as fm
import BasisFunktionen as bf





mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0, 0, 0)
mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 1, [0, -50, 0], 0, 0, 0)
mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 1, [0, 50, 0], np.pi/2, 0, 0)

mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
# ([mesh3D_Arrow_1])
# fig = go.Figure(data=mesh3D_Differential_element_1)
fig = go.Figure(data=mesh3D_Differential_element_1)
fig.show()
fig.write_html("./file.html")



# CSS color:
#                 aliceblue, antiquewhite, aqua, aquamarine, azure,
#                 beige, bisque, black, blanchedalmond, blue,
#                 blueviolet, brown, burlywood, cadetblue,
#                 chartreuse, chocolate, coral, cornflowerblue,
#                 cornsilk, crimson, cyan, darkblue, darkcyan,
#                 darkgoldenrod, darkgray, darkgrey, darkgreen,
#                 darkkhaki, darkmagenta, darkolivegreen, darkorange,
#                 darkorchid, darkred, darksalmon, darkseagreen,
#                 darkslateblue, darkslategray, darkslategrey,
#                 darkturquoise, darkviolet, deeppink, deepskyblue,
#                 dimgray, dimgrey, dodgerblue, firebrick,
#                 floralwhite, forestgreen, fuchsia, gainsboro,
#                 ghostwhite, gold, goldenrod, gray, grey, green,
#                 greenyellow, honeydew, hotpink, indianred, indigo,
#                 ivory, khaki, lavender, lavenderblush, lawngreen,
#                 lemonchiffon, lightblue, lightcoral, lightcyan,
#                 lightgoldenrodyellow, lightgray, lightgrey,
#                 lightgreen, lightpink, lightsalmon, lightseagreen,
#                 lightskyblue, lightslategray, lightslategrey,
#                 lightsteelblue, lightyellow, lime, limegreen,
#                 linen, magenta, maroon, mediumaquamarine,
#                 mediumblue, mediumorchid, mediumpurple,
#                 mediumseagreen, mediumslateblue, mediumspringgreen,
#                 mediumturquoise, mediumvioletred, midnightblue,
#                 mintcream, mistyrose, moccasin, navajowhite, navy,
#                 oldlace, olive, olivedrab, orange, orangered,
#                 orchid, palegoldenrod, palegreen, paleturquoise,
#                 palevioletred, papayawhip, peachpuff, peru, pink,
#                 plum, powderblue, purple, red, rosybrown,
#                 royalblue, saddlebrown, salmon, sandybrown,
#                 seagreen, seashell, sienna, silver, skyblue,
#                 slateblue, slategray, slategrey, snow, springgreen,
#                 steelblue, tan, teal, thistle, tomato, turquoise,
#                 violet, wheat, white, whitesmoke, yellow,
#                 yellowgreen