from pathlib import Path

import pyvips


def split_image(
    img_path: str,
    output_dir: str,
    tile_size: int,
    quality: int,
) -> None:
    img_suffix = Path(img_path).suffix

    image = pyvips.Image.new_from_file(img_path, access="sequential")
    image.dzsave(
        output_dir,
        tile_size=tile_size,
        suffix=f".{img_suffix}[Q={quality}]",
    )


def compress(
    img_path: str,
    output_dir: str,
) -> None:
    img_path = Path(img_path)
    output_dir = Path(output_dir)
    image = pyvips.Image.new_from_file(img_path)

    image.write_to_file(
        output_dir / img_path.stem + img_path.suffix,
        predictor="horizontal",
        compression="deflate",
    )
