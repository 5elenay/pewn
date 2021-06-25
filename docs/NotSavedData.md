# NotSavedData

Not saved data class. If you don't add option when you use download function, You will get this class.

# Attributes

- `data` - Your data.
  - Default: `Your data.`
  - Type: `bytes`
- `url` - URL for data.
  - Default: `URL for data.`
  - Type: `str`
- `size` - Data size in byte.
  - Default: `Data size in byte.`
  - Type: `int`

# Functions

## write

Write data to file.

- Parameters:

  - option (`Option`): `<Option>` object.

- Returns:
  - `str`: Saved path.
- Example:
  ```py
  result = await pewn.download("https://picsum.photos/500/300") # -> <NotSavedData>

  result.write(pewn.Option(
      file_name="photo.png",
      folder=("my", "photo", "folder", "location", )
  ))
  ```
