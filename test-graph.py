from mlx import Mlx
import os

def on_key(key, p): print(key)

def on_key(key, param):
    if key == 65307: # ESC key
        os._exit(0)

def kill_window(key, param):
    if key == 50: # 2 key
        mlx.mlx_destroy_image(param["mlx_ptr"], param["img_ptr"])

def main() -> None:
    mlx = Mlx()
    mlx_ptr = mlx.mlx_init()
    win_ptr = mlx.mlx_new_window(mlx_ptr, 800, 800, "Primera Janela")

    mlx.mlx_key_hook(win_ptr, on_key, None)
    mlx.mlx_hook(win_ptr, 33, 0, lambda p: os._exit(0), None) # Close Button

    # for y in range(300, 400):
    #     for x in range(200, 300):
    #         mlx.mlx_pixel_put(mlx_ptr, win_ptr, y, x, 0xFFFFFFFF) #mlx_pixel_put should not be used, since it is not performatic

    img_ptr = mlx.mlx_new_image(mlx_ptr, 800, 800)

    data, bpp, size_line, fmt = mlx.mlx_get_data_addr(img_ptr)

    # # Put a white pixel at (10, 20)
    # offset = 20 * size_line + 10 * 4
    # data[offset:offset + 4] = bytes([0xFF, 0xFF, 0xFF, 0xFF])

    # Fill entire image red
    for offset in range(0, size_line * 800, 4):
        data[offset:offset + 4] = bytes([0xDB, 0x3F, 0x33, 0xFF])

    mlx.mlx_put_image_to_window(mlx_ptr, win_ptr, img_ptr, 0, 0)

    mlx.mlx_string_put(mlx_ptr, win_ptr, 100, 50, 0xFFFFFFFF, "Hello World")

    mlx.mlx_loop(mlx_ptr)

if __name__ == "__main__":
    main()
