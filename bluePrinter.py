from turtle import position
from PIL import Image
import json


def add_pattern(position: tuple, pattern_img: Image, dest_img: Image):
    width, height = pattern_img.size
    for row_idx in range(height):
        for col_idx in range(width):
            px = position[0]+col_idx
            py = position[1]+row_idx
            dest_img.putpixel((px*3+1, py*3+1),
                              pattern_img.getpixel((col_idx, row_idx)))


def generate_config():
    conf_d = {"p1": {'file_path': 'p1.png', "position_x": 1, "position_y": 2},
              "p2": {'file_path': 'p2.png', "position_x": 500, "position_y": 500}
              }
    with open('config.json', 'w') as f:
        f.write(json.dumps(conf_d))


def get_config():
    with open('config.json', 'r') as f:
        return json.loads(f.read())


if __name__ == "__main__":
    conf_d = get_config()
    dest_img = Image.new('RGBA', (3000, 3000))
    for key in conf_d:
        pattern_img = Image.open(conf_d[key]['file_path'])
        position = (conf_d[key]['position_x'], conf_d[key]['position_y'])
        add_pattern(position, pattern_img, dest_img)
    dest_img.save('blue_print.png')
