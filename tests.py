from color import *
from color_names import *


def test(actual, expected):
    if actual != expected:
        raise Exception(
            'Test failed: expected {0} but actual is {1}!'
            .format(expected, actual)
        )


# HEX
# Correct input data
test(parse_hex_color('#000000'), hex_to_int('000000'))
test(parse_hex_color('000000'), hex_to_int('000000'))
test(parse_hex_color('#000'), hex_to_int('000000'))
test(parse_hex_color('012'), hex_to_int('001122'))
test(parse_hex_color('00 00 00'), hex_to_int('000000'))
test(parse_hex_color('# 00 00 00'), hex_to_int('000000'))

# Incorrect input data
test(parse_hex_color(''), None)


# RGB
# Correct input data
test(parse_rgb_color('rgb  (0, 00, 000)'), 0)
test(parse_rgb_color('rgb( 0, 00, 000)'), 0)
test(parse_rgb_color('0, 00, 000'), 0)
test(parse_rgb_color('0.0, 00, 000'), 0)
test(parse_rgb_color('0, 0, 0'), 0)
test(parse_rgb_color('0; 0; 0'), 0)
test(parse_rgb_color('0;0;0'), 0)
test(parse_rgb_color('0,0,0'), 0)
test(parse_rgb_color('0;0; 0'), 0)
test(parse_rgb_color('0.0 ; 0.0;0.0'), 0)
test(parse_rgb_color('0.0, 0.0, 0.0'), 0)
test(parse_rgb_color('0,0; 0,0; 0,0'), 0)
test(parse_rgb_color('0,0 0,0 0,0'), 0)
test(parse_rgb_color('0,0   0,0 0,0'), 0)
test(parse_rgb_color('00 0.0 0.0'), 0)

# Incorrect input
test(parse_rgb_color('0.0 0,0 0,0'), None)
test(parse_rgb_color('0,0, 0,0, 0,0'), None)
test(parse_rgb_color('2 0.0 0.0'), None)


test(find_color_by_name('aqua'), find_color_by_name_exact('Aqua'))
test(find_color_by_name('aqia'), find_color_by_name_exact('Aqua'))
test(find_color_by_name('aqu'), find_color_by_name_exact('Aqua'))
test(find_color_by_name('aqva'), find_color_by_name_exact('Aqua'))
test(find_color_by_name('aquaa'), find_color_by_name_exact('Aqua'))
test(find_color_by_name('akua'), find_color_by_name_exact('Aqua'))




