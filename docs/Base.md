# Attributes

- `__version__` - Pewn Version.
- `__github__` - Pewn Source Code.

# Functions

## download

Download data from URL.

- Parameters:

  - url (`str`): URL for fetch and download.
  - option (`Option`): `<Option>` object. **Optional**

- Returns:
  - `str`: Saved path.
  - `NotSavedData`: `<NotSavedData>` object if you don't add option parameter.
- Example:
  ```py
  await pewn.download("https://picsum.photos/500/300", pewn.Option(
      file_name = "photo.png",
      folder = ["photos", "random"] # Also you can use "./photos/random"
      # folder = "./photos/random"
  )) # -> ./photos/random/photo.png
  ```
  ```py
  result = await pewn.download("https://picsum.photos/500/300") # -> <NotSavedData>
  ```

# Classes

- [Option](https://github.com/5elenay/pewn/blob/main/docs/Option.md)
- [NotSavedData](https://github.com/5elenay/pewn/blob/main/docs/NotSavedData.md)
