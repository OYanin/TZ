from sys import argv

def calc_distance(path_circle, path_dot):

    with open(path_circle, 'r') as f_circle:
        tmp = f_circle.readlines()
        circle_centre = tuple(map(int, tmp[0].split())) #(1, 1)
        circle_radius = int(tmp[1]) #5
        del tmp

    with open(path_dot, 'r') as f_dot:
        dots = [tuple(map(int, i.replace('\n', '').split())) for i in f_dot.readlines()]

    for dot in dots:
        distance = ((circle_centre[0] - dot[0])**2+(circle_centre[1] - dot[1])**2)**0.5
        if distance == circle_radius:
            print(0)    #на окружности
        elif distance > circle_radius:
            print(2)    #снаружи
        else:
            print(1)    #внутри

calc_distance(argv[1], argv[2])
