# dateandtimeparser

-----

**Table of Contents**

* [Installation](#installation)
* [License](#license)

## Installation

dateandtimeparser is distributed on [PyPI](https://pypi.org) as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.6+.

```bash
$ pip install dateandtimeparser
```

## Usage

```python
from dateandtimeparser import DateTimeParser as parser

text = 'Today is 10/12/16 and tomorrow is January 01 2019.'
dp = parser(text, start_year=2000, end_year=2020)
```

## License

dateandtimeparser is distributed under the terms of the
[MIT License](https://choosealicense.com/licenses/mit).
