def hex_interpreter(h):
    h = h.lstrip('#')
    return list(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_interpreter(rgb):
    return '#%02x%02x%02x' % rgb

def lighten(h, percent):
    color = hex_interpreter(h)
    goal_1 = color[0] + (255 - color[0]) * percent // 100
    goal_2 = color[1] + (255 - color[1]) * percent // 100
    goal_3 = color[2] + (255 - color[2]) * percent // 100
    print(color)
    print(goal_1, goal_2, goal_3)
    color = (goal_1, goal_2, goal_3)
    return rgb_interpreter(color)

def darken(h, percent):
    color = hex_interpreter(h)
    goal_1 = color[0] * percent // 100
    goal_2 = color[1] * percent // 100
    goal_3 = color[2] * percent // 100
    print(color)
    print(goal_1, goal_2, goal_3)
    color = (goal_1, goal_2, goal_3)
    return rgb_interpreter(color)
