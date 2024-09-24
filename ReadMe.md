# Installation
Run the following command in your terminal:
```bash
pip install -r requirements.txt
```

# Usage
## Basic Usage
Simply change your working path in `run.py`, and then run the script.
## Advanced Usage
If you'd like to change the weight of each operation, you can do so in `processing.py`. Modify the values as needed. The default settings are as follows:

| operation        | default | descr                          |
|------------------|---------|--------------------------------|
| flip_upside_down | 0.5     | Flip your image upside-down    |
| flip_left_right  | 0.5     | Flip your image left to right  |
| rotate_90        | 0.5     | Rotate your image 90 degrees   |
| rotate_180       | 0.5     | Rotate your image 180 degrees  |
| rotate_270       | 0.5     | Rotate your image 270 degrees  |
| gaussian_blur    | 0.35    | Apply Gaussian blur            |
| add_noise        | 0.35    | Add random noise to the image  |
| stretch          | 0.2     | Stretch the image dimensions   |
| invert_colors    | 0.05    | Invert the colors of the image |
| edge_detection   | 0.05    | Apply edge detection filter    |

