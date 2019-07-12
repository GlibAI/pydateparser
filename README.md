# pydateparser

-----

**Table of Contents**

* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

## Installation

pydateparser is distributed on [PyPI](https://pypi.org) as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.6+.

```bash
$ pip install pydateparser
#or
$ python setup.py install
```

## Usage

sample input:
```python
from pydateparser import DateParser as parser

text = 'Today is 10/12/16 and tomorrow is January 01 2019.'
dp = parser(text, start_year=2000, end_year=2020, datetime_format=None)
```
sample output: 
```python
dp.datetime

#output
[datetime(date='january 01 2019', token_span=(34, 49), token_index=(6, 8), format='%B %d %Y'),
 datetime(date='10/12/16', token_span=(9, 17), token_index=(2, 2), format='%d/%m/%y')]
```
for an extended usage demo refer [this](https://github.com/GlibAI/pydateparser/blob/master/notebooks/lib-usage-notebook.ipynb) notebook.
## License

pydateparser is distributed under the terms of the
[MIT License](https://choosealicense.com/licenses/mit).
