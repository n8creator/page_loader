[![Github Actions Status](https://github.com/n8creator/python-project-lvl3/workflows/Python%20CI/badge.svg)](https://github.com/n8creator/python-project-lvl3/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/072130a43f1b95851ea6/maintainability)](https://codeclimate.com/github/n8creator/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/072130a43f1b95851ea6/test_coverage)](https://codeclimate.com/github/n8creator/python-project-lvl3/test_coverage)
[![Actions Status](https://github.com/n8creator/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/n8creator/python-project-lvl3/actions)

# Page Loader CLI
Page Loader utility allows to download some page and associated files (img, css, js, etc.) from the Web and save it into specified directory (current directory used by default).


## Installation
Install via `pip` package manager:
```bash
pip install --user git+https://github.com/n8creator/python-project-lvl3.git
```

## Usage
### As a library function
```python
from page_loader import download

file_path = download('https://www.python.org/', '/var/tmp')
print(file_path)  # => '/var/tmp/www-python-org.html'
```

### As a command-line utility
```bash
$ page-loader https://www.python.org/ -o /var/tmp/

# Output
Index page 'https://www.python.org/' was downloaded!
Loading resourses: |████████████████████████████████| 15/15
Output page had been saved to '/var/tmp/www-python-org.html'
```

## Examples of usage
[![asciicast](https://asciinema.org/a/Wgh6hNzpaIeDbtEiAZTUVC4Km.svg)](https://asciinema.org/a/Wgh6hNzpaIeDbtEiAZTUVC4Km)
