import json
import colorsys


def convert_to_rgba(colors: dict):
    converted = {}

    for k, v in colors.items():
        # print(k , v)
        inside_paren = v[v.find("(")+1:v.find(")")].split(', ')
        h = (int(inside_paren[0])) / 360
        s = int(inside_paren[1].replace('%', '')) / 100
        l = int(inside_paren[2].replace('%', '')) / 100
        a = 1.0
        if len(inside_paren) == 4:
            a = float(inside_paren[3])
        # print(h, s, l, a)

        rgba_float = (*colorsys.hls_to_rgb(h, l, s), a)
        # print(rgba_float)
        rgba_hex = '#'
        for c in rgba_float:
            hx = hex(int(c * 255))
            rgba_hex += hx[-2:]
        # print(rgba_hex)

        converted[k] = rgba_hex

    return converted


if __name__ == '__main__':
    with open('/Users/adam/Desktop/sublime_sixteen.json') as f:
        data = json.load(f)

    colors = set()
    for r in data['rules']:
        # print(r['name'])
        # print(r)
        try:
            colors.add(r['foreground'])
        except:
            pass
        # print()
    print(colors)
