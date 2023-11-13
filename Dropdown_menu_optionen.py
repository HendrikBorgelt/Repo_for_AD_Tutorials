def create_drop_menu_dicts(three_d_Objects, display_options, frame_options):
    visible = []
    visibilities= dict(visible=[])
    annotations= []
    list_of_geometry_numbers = [13, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    for i_1, i_2  in enumerate(three_d_Objects):
        visible.append([three_d_Objects[i_1]]*list_of_geometry_numbers[i_1])

        # dict(label="Geometry Beschriftet",
        #      method="relayout",
        #      args=[{"scene.annotations": geometry_annotations}]),
    visibilities['visible']= sum(visible, [])
    return visibilities