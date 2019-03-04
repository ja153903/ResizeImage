# pip install Pillow if you lack dependency
from PIL import Image
import os


def resize_image(image_path, new_dim):
    try:
        # Create image object and resize image to new dimension
        img = Image.open(image_path)
        resized_img = img.resize((new_dim, new_dim))

        # Find the full path and extension so we can create new output path
        path_wout_ext, ext = os.path.splitext(image_path)
        output_path = f'{path_wout_ext}_result_{new_dim}x{new_dim}{ext}'

        # Save re-sized image to output path
        resized_img.save(output_path)

        print(f'Image saved at output path: {output_path}')
    except FileNotFoundError:
        print(f'File in path {image_path} does not exist')


if __name__ == '__main__':
    while True:
        file_path = input('Enter a valid absolute filepath: ')
        if os.path.exists(file_path):
            break

    dim = int(input('Enter dimension of square image: '))
    assert isinstance(dim, int)
    resize_image(file_path, dim)
