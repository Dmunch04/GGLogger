# GGLogger
A function logger for Python

See examples under `Examples/Example.py`

Supported return types:
- Int
- Float
- String
- List
- Dict
- Tuple
- Or use combine to combine 2 or more types

<br><br>

# Functions
## Print Function
*RIGHT NOW PRINT ONLY WORKS ON COMBINED FUNCTIONS!*
Use:
```py
@GG.Print
@GG.Combine (int, str, list)
def Test ():
  if 0:
    return [0]

  elif 1:
    return str (0)

  else:
    return int (0)

# Output result:
# [0]
```

## Log Function
Use:
```py
@GG.Int
@GG.Log ()
def Test ():
    return 1

# Output result:
# ----- Log Result -----
# Executed:           Test
# Result:             1
# Result Type:        str
# Execution Time:     0.0 seconds
# Arg Count:          0
# File Path:          C:\Path\To\File.py
# Start Line:         1
# ----------------------
```
