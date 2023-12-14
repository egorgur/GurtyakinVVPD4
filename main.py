def hex_interpreter(h):
    h = h.lstrip('#')
    return list(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_interpreter(rgb):
    return '#%02x%02x%02x' % rgb