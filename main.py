from pathlib import Path
import sys

from PIL import Image
import numpy as np


def convert_image_to_bin(input_path: Path, output_path: Path) -> None:
    img = Image.open(input_path).convert("RGB")
    img_data = np.array(img)
    with open(output_path, "wb") as file:
        file.write(img_data)


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python main.py <input_image> [output_bin]")

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".bin")
    convert_image_to_bin(input_path, output_path)


if __name__ == "__main__":
    main()
