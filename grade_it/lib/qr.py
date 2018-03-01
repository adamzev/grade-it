import os
import pkg_resources
import glob


import qrcode

def get_qr_code(data, file_prefix, size="normal", file_ext="png"):
    file_dir = os.path.dirname(os.path.realpath('__file__'))

    sizes = {
        "large" : 3,
        "normal": 2,
        "small": 1
    }
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = sizes[size],
        border = sizes[size] + 2,
    )

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    os.path.abspath(os.path.join(file_dir, os.pardir, os.pardir))
    file_dir = os.path.join(file_dir, os.pardir)
    folder = os.path.join(file_dir, "img", "qr")
    print(folder)
    files = glob.glob("{}/{}*.{}".format(folder, file_prefix, file_ext))
    file_nums = [0]
    for file_ in files:
        file_num = file_[-7:-4]
        file_nums.append(int(file_num))
    number = max(file_nums) + 1
    if number > 99999:
        number = 1
    file_name = "{}/{}_{}.{}".format(folder, file_prefix, str(number).zfill(5), file_ext)
    img.save(file_name)
    return file_name