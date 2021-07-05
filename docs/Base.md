# Attributes

- `__version__` - Pewn Version.
- `__github__` - Pewn Source Code.

# Functions

## download

Download data from URL.

- Parameters:

  - url (`str`): URL for fetch and download.
  - option (`Option`): `<Option>` object. **Optional**
  - `**kwargs`: Parameters for aiohttp get function. (proxy etc...)

- Returns:
  - `str`: Saved path.
  - `NotSavedData`: `<NotSavedData>` object if you don't add option parameter.
- Example:
  ```py
  await pewn.download("https://picsum.photos/500/300", pewn.Option(
    file_name = "photo.png",
    folder = ("photos", "random", ) # Also you can use "./photos/random"
    # folder = "./photos/random"
  )) # -> ./photos/random/photo.png
  ```
  ```py
  result = await pewn.download("https://picsum.photos/500/300") # -> <NotSavedData>
  ```

## download_multiple

Download multiple file async.

- Parameters:

  - urls (`tuple`): URLs for fetch and download.
  - options (`tuple, Option`): `<Option>` objects in tuple or only one `<Option>` object. **Optional**
  - `**kwargs`: Parameters for aiohttp get function. (proxy etc...)

- Returns:
  - `list` (`str`): Saved paths.
  - `list` (`NotSavedData`): List of `<NotSavedData>` object if you don't add options parameter.
- Example:
  ```py
  result = await pewn.download_multiple(
    tuple(["https://picsum.photos/500/300" for _ in range(10)]),
    pewn.Option(
      file_name = "photo.png",
      folder = "./photos/random"
    )
  ) # -> ["./photos/photo_1.png", "./photos/photo_2.png", ...]
  ```
  ```py
  result = await pewn.download_multiple(
    ("https://picsum.photos/500/300", "https://picsum.photos/500/300"),
    (
      pewn.Option(
        file_name = "photo_one.png",
        folder = "./photos/random"
      ),
      pewn.Option(
        file_name = "photo_two.png",
        folder = ("photos", "random", )
      )
    )
  ) # -> ["./photos/photo_one.png", "./photos/photo_two.png"]
  ```
  ```py
  result = await pewn.download_multiple(
    tuple(["https://picsum.photos/500/300" for _ in range(25)])
  ) # -> [<NotSavedData>, <NotSavedData>, ...]
  ```

# Classes

- [Option](https://github.com/5elenay/pewn/blob/main/docs/Option.md)
- [NotSavedData](https://github.com/5elenay/pewn/blob/main/docs/NotSavedData.md)
