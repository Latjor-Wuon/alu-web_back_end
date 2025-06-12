# Python Variable Annotations

This project focuses on understanding and implementing type annotations in Python 3, including function signatures, variable types, and code validation using mypy.

## Learning Objectives

By the end of this project, you will be able to explain:

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing concepts
- How to validate your code with mypy

## Resources

### Read or Watch:
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Requirements

### General
- **Allowed editors**: vi, vim, emacs
- **Environment**: Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project is mandatory
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- File length will be tested using `wc`
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation
- Documentation should be meaningful sentences explaining the purpose

## Project Structure

```
python_variable_annotations/
├── README.md
├── 0-add.py
├── 1-concat.py
├── 2-floor.py
├── 3-to_str.py
├── 4-define_variables.py
├── 5-sum_list.py
├── 6-sum_mixed_list.py
├── 7-to_kv.py
├── 8-make_multiplier.py
└── 9-element_length.py
```

## Tasks Overview

### 0. Basic annotations - add
Write a type-annotated function `add` that takes two floats and returns their sum.

### 1. Basic annotations - concat
Write a type-annotated function `concat` that concatenates two strings.

### 2. Basic annotations - floor
Write a type-annotated function `floor` that returns the floor of a float.

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that converts a float to string.

### 4. Define variables
Define and annotate variables with specified values and types.

### 5. Complex types - list of floats
Write a function that sums a list of floats using type annotations.

### 6. Complex types - mixed list
Write a function that sums a mixed list of integers and floats.

### 7. Complex types - string and int/float to tuple
Write a function that returns a tuple with a string and squared number.

### 8. Complex types - functions
Write a function that returns another function (higher-order function).

### 9. Let's duck type an iterable object
Annotate function parameters and return values for an iterable processing function.

## Usage Examples

### Basic Type Annotations
```python
def add(a: float, b: float) -> float:
    """Add two floats and return the sum."""
    return a + b
```

### Complex Type Annotations
```python
from typing import List, Union, Tuple, Callable

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of integers and floats."""
    return sum(mxd_lst)
```

## Testing

To test your implementations:

1. Make files executable:
   ```bash
   chmod +x *.py
   ```

2. Run individual test files:
   ```bash
   ./0-main.py
   ./1-main.py
   # ... etc
   ```

3. Validate with mypy:
   ```bash
   mypy 0-add.py
   mypy 1-concat.py
   # ... etc
   ```

## Code Style

Ensure your code follows pycodestyle:
```bash
pycodestyle *.py
```

## Documentation Testing

Test module documentation:
```bash
python3 -c 'print(__import__("0-add").__doc__)'
```

Test function documentation:
```bash
python3 -c 'print(__import__("0-add").add.__doc__)'
```

## Repository Information

- **GitHub repository**: alu-web_back_end
- **Directory**: python_variable_annotations

## Author

This project is part of the ALU Web Backend curriculum focusing on Python type annotations and static type checking.
