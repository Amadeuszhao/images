import os
import json
from PIL import Image

# 配置文件夹路径和输出JSON文件路径
image_folder = 'F:\Amadeuszhao.github.io\images\\singapore'
output_json_file = 'output_singapore.json'
base_url = 'https://raw.githubusercontent.com/Amadeuszhao/Amadeuszhao.github.io/main/images/singapore/'
default_type = '2'

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size

def create_image_json(image_path):
    width, height = get_image_dimensions(image_path)
    # 如果宽或高超过1920，则进行等比例缩小
    if width > 1920 or height > 1920:
        if width >= height:
            ratio = 1920 / width
        else:
            ratio = 1920 / height
        middle_width = int(width * ratio)
        middle_height = int(height * ratio)
    else:
        middle_width = width
        middle_height = height
    
    small_width = middle_width // 2
    small_height = middle_height // 2
    image_name = os.path.basename(image_path)
    
    return {
        "small": base_url + image_name,
        "middle": base_url + image_name,
        "small_width": small_width,
        "small_height": small_height,
        "middle_width": middle_width,
        "middle_height": middle_height,
        "desc": image_name,
        "type": default_type,
        "name": image_name,
        "id": image_name
    }

image_json_list = []

for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image_path = os.path.join(image_folder, filename)
        image_json = create_image_json(image_path)
        image_json_list.append(image_json)

with open(output_json_file, 'w') as json_file:
    json.dump(image_json_list, json_file, indent=4)

print(f'JSON文件生成完毕: {output_json_file}')