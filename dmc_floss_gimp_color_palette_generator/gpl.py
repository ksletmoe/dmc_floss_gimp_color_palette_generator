# -*- coding: utf-8 -*-
import typing


class Color:
    def __init__(self, r: str, g: str, b: str, name: typing.Optional[str] = None):
        self.r: str = r
        self.g: str = g
        self.b: str = b
        self.name: str = name

    def render(self) -> str:
        line = f"{self.r} {self.g} {self.b}"
        if self.name:
            line = f"{line} {self.name}"

        return line


class GimpColorPalette:
    """
    Defines a GIMP color palette file (.gpl). The format is undocumented but the source is here:
    https://gitlab.gnome.org/GNOME/gimp/-/blob/gimp-2-10/app/core/gimppalette-load.c#L39

    Basically a header with a bunch of color lines where each line follows the format:
    <r value> <g value> <b value> [optional name]
    """

    def __init__(self, name: str):
        self.name: str = name
        self.colors: typing.List[Color] = []

    def add_color(self, color: Color):
        self.colors.append(color)

    def render(self) -> str:
        header = "\n".join(
            [
                "GIMP Palette",
                f"Name: {self.name}",
                "Columns: 1",  # this is just the default display setting for the palette
                "#",
            ]
        )

        return "\n".join([header, *[c.render() for c in self.colors]])
