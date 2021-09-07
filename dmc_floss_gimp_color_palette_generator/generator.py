# -*- coding: utf-8 -*-
import pathlib
import sys
import traceback

import requests
from bs4 import BeautifulSoup

from . import gpl

GPL_DATA_ENDPOINT = "http://my.crazyartzone.com/dmc.asp"
COLOR_PALETTE_NAME = "DMC Floss"
COLOR_PALETTE_FILE_PATH = pathlib.Path("dmc_floss.gpl")


def get_data() -> str:
    response = requests.get(GPL_DATA_ENDPOINT)

    if not response.ok:
        raise RuntimeError(
            f"Got a non-2XX response from endpoint: [{response.status_code}] {response.text}"
        )

    return response.text


def run():
    try:
        palette_file_path = (
            pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else COLOR_PALETTE_FILE_PATH
        )

        gpl_data_str = get_data()
        data_soup = BeautifulSoup(gpl_data_str, "html.parser")
        palette = gpl.GimpColorPalette(COLOR_PALETTE_NAME)

        # page should have just the one table
        for idx, row in enumerate(data_soup.find_all("tr")):
            if idx == 0:
                # don't care about the TH
                continue

            cells = row.find_all("td")
            color_name = f"{cells[2].a.string} (DMC {cells[1].string})"  # name (DMC ID)

            palette.add_color(
                gpl.Color(cells[3].string, cells[4].string, cells[5].string, color_name)
            )

        palette_file_path.write_text(palette.render(), "utf-8")

        print(f"Wrote DMC floss palette file '{palette_file_path.absolute()}'")
    except Exception:
        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    run()
