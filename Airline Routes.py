import folium
from folium.plugins import AntPath


def main():
    """
    Read the routes file and take records on each planes route

    """
    p1_route = []
    p2_route = []
    p3_route = []
    p4_route = []

    with open('Routes.csv', 'r') as f:
        lines = f.readlines()

        for line in lines:
            info = [item.strip() for item in line.strip().split('-')]
            depairport = info[0]
            arrairport = info[1]
            plane = info[2]
            if plane == 'AC110':
                lst = rec_coor(depairport, arrairport)
                for i in lst:
                    p1_route.append(i)

            elif plane == 'AC350':
                lst = rec_coor(depairport, arrairport)
                for i in lst:
                    p2_route.append(i)
            elif plane == 'AC400':
                lst = rec_coor(depairport, arrairport)
                for i in lst:
                    p3_route.append(i)
            else:
                lst = rec_coor(depairport, arrairport)
                for i in lst:
                    p4_route.append(i)

    visualizer(p1_route, p2_route, p3_route, p4_route, "blue"
               , "purple", "red", "green")


def rec_coor(depart: str, arrival: str) -> [(float, float), (float, float)]:

    lst = []

    airports = {'Toronto': (43.6777, -79.6248),
                'Vancouver': (49.1947, -123.1792),
                'Calgary': (51.1314, -114.0103),
                'Montreal': (45.4577, -73.7499),
                'New York': (40.641300, -73.778100),
                'Los Angeles': (33.941600, -118.408500),
                'California': (37.621300, -122.379000),
                'Miami': (25.793200, -80.290600)}

    for key in airports.keys():
        if key == depart:
            coors1 = (airports[depart])
            lst.append(coors1)
        elif key == arrival:
            coors2 = (airports[arrival])
            lst.append(coors2)

    return lst


def visualizer(lst1, lst2, lst3, lst4, color1, color2, color3, color4):
    map_obj = folium.Map(location=[56.1304, -106.3468], zoom_start=5)

    pathlatlngs = [(43.677700, -79.624800), (49.194700, -123.179200)]

    AntPath(lst1, delay=400, weight=8, color=color1,
            dash_array=[30, 15]).add_to(map_obj)

    AntPath(lst2, delay=400, weight=8, color=color2,
            dash_array=[30, 15]).add_to(map_obj)

    AntPath(lst3, delay=400, weight=8, color=color3,
            dash_array=[30, 15]).add_to(map_obj)

    AntPath(lst4, delay=400, weight=8, color=color4,
            dash_array=[30, 15]).add_to(map_obj)

    map_obj.save("output2.html")


if __name__ == "__main__":
    main()
