# Artwork

Artwork is a Python CLI Application for downloading the highest quality album artworks using the iTunes API.

## Installation

Download the source code. In the directory run:

```bash
pip install -r requirements.txt
```

## Usage

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ Artwork - Album Art Downloader v1.0                                                     │
└─────────────────────────────────────────────────────────────────────────────────────────┘
 Search <q to quit>: Radiohead OK Computer
┌───┬────────────────────────┬────────────────────────────────────────────────────────────┐
│ # │         Artist         │                           Album                            │
├───┼────────────────────────┼────────────────────────────────────────────────────────────┤
│ 1 │       Radiohead        │                        OK Computer                         │
│ 2 │       Radiohead        │               OK Computer OKNOTOK 1997 2017                │
│ 3 │ Vitamin String Quartet │     Strung Out On OK Computer: VSQ Performs Radiohead      │
│ 4 │ Molotov Cocktail Piano │ MCP Performs Radiohead: OK Computer (Instrumental Version) │
└───┴────────────────────────┴────────────────────────────────────────────────────────────┘
 Selection <q to quit>: 1
 Save to/as: art
 File successfully downloaded.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)