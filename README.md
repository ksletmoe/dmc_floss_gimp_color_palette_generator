# dmc-floss-gimp-color-palette-generator
Generates a GIMP palette from the data at http://my.crazyartzone.com/dmc.asp

You can install this tool to generate the latest color palette data. DMC doesn't release new colors
all that often however, so you may just want to download the latest pre-generated palette from [palettes/](palettes/).

## Installation
`$ pip install dmc-floss-gimp-color-palette-generator`

## Usage
`$ generate_dmc_palette`

The above will write out a palette file called `dmc_floss.gpl` in the current working directory.

Alternatively, you can specify the output file path:
`$ generate_dmc_palette /some/file/path.gpl`

Be sure to keep the extension as `.gpl` so GIMP will recognize it as a palette file.

## Importing a palette file into GIMP
Right click somewhere in the Palettes dialog and click "Import Palette...". In the resulting dialog,
click "Palette File" and select the palette file with the file selection dialog. Be sure to set the
desired name for your palette in the "Palette Name" text box. Click "Import" and your palette will
be usable in GIMP.

![Import Palette Dialog](https://github.com/ksletmoe/dmc_floss_gimp_color_palette_generator/blob/main/readme/import_palette.png?raw=true)
