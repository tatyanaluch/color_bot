from string import hexdigits


def parse_hex_color(data):
    color = data.strip().upper()

    if color.startswith('#'):
        color = color[1:].lstrip()

    components = color.split(' ')

    if all(is_hex_string(element) for element in components):
        if len(components) == 1:
            hex_str = components[0]
        elif len(components) == 3:
            for element in components:
                if len(element) != 2:
                    return None
            hex_str = ''.join(components)
        else:
            return None

        if len(hex_str) == 6:
            return hex_to_int(hex_str)

        if len(hex_str) == 3:
            return hex_to_int('{0}{0}{1}{1}{2}{2}'.format(
                hex_str[0], hex_str[1], hex_str[2]
            ))

    return None


def is_hex_string(string):
    return all(char in hexdigits for char in string)


def hex_to_int(hex_str):
    return int(hex_str, 16)


def int_to_hex(color):
    return hex(color)


def parse_rgb_color(data):
    color = data.strip().upper()

    if color.startswith('RGB'):
        color = color[3:].strip()

    if color.startswith('(') and color.endswith(')'):
        color = color[1: -1].strip()

    result = try_parse_rgb_color(color, ';')
    if result is not None:
        return result

    result = try_parse_rgb_color(color, ',')
    if result is not None:
        return result

    result = try_parse_rgb_color(color, ' ')
    if result is not None:
        return result

    return None


def try_parse_rgb_color(color, separator):
    components = split_and_strip(color, separator)
    if len(components) != 3:
        return None

    has_point = False
    has_comma = False

    for x in components:
        if '.' in x:
            has_point = True
        if ',' in x:
            has_comma = True

    if has_point and has_comma:
        return None

    if has_comma:
        components = list(map(lambda y: y.replace(',', '.'), components))
        has_comma = False
        has_point = True

    if has_point:
        red = try_parse_float(components[0])
        green = try_parse_float(components[1])
        blue = try_parse_float(components[2])

        if is_float_component(red) and is_float_component(green) and is_float_component(blue):
            return rgb_floats_to_int(red, green, blue)

    else:
        red = try_parse_int(components[0])
        green = try_parse_int(components[1])
        blue = try_parse_int(components[2])

        if is_int_component(red) and is_int_component(green) and is_int_component(blue):
            return rgb_ints_to_int(red, green, blue)

    return None


def split_and_strip(string, separator):
    split = string.split(separator)
    if separator == ' ':
        split = list(filter(lambda x: x != '', split))
    else:
        split = list(map(lambda x: x.strip(), split))
    return split


def try_parse_float(x):
    try:
        return float(x)
    except ValueError:
        return None


def try_parse_int(x):
    try:
        return int(x)
    except ValueError:
        return None


def is_float_component(x):
    if x is not None:
        if 0 <= x <= 1:
            return True
    return False


def is_int_component(x):
    if x is not None:
        if 0 <= x <= 255:
            return True
    return False


def rgb_floats_to_int(r, g, b):
    red = int(r * 255)
    green = int(g * 255)
    blue = int(b * 255)
    return rgb_ints_to_int(red, green, blue)


def rgb_ints_to_int(r, g, b):
    return (r << 16) + (g << 8) + b


def print_hex_color(color):
    return '#{:02X}{:02X}{:02X}'.format(
        red_component(color),
        green_component(color),
        blue_component(color)
    )


def print_rgb_int_color(color):
    return '({}, {}, {})'\
        .format(
            red_component(color),
            green_component(color),
            blue_component(color))


def print_rgb_float_color(color):
    return '({:.2}, {:.2}, {:.2})' \
        .format(
            red_component(color) / 255,
            green_component(color) / 255,
            blue_component(color) / 255)


def red_component(color):
    return (color >> 16) % 256


def green_component(color):
    return (color >> 8) % 256


def blue_component(color):
    return color % 256
