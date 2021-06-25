# Option

Set options for downloading files.

## Example:

```py
pewn.Option(
    file_name = "index.html",
    folder = "./downloaded" # ("downloaded", )
)
```

# Init

- file_name (`str`): File name.
- folder (`str`, `tuple`): Folder tuple or path-like string.
  - Example: `("images", "random", )` is `./images/random`
  - Also you can use like this: `./images/random`

# Attributes

- `file_name` - File name.
  - Default: `Same with your file name.`
  - Type: `str`
- `folder` - Converted folder.
  - Default: `Converted version of folder.`
  - Type: `str`
