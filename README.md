<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/elapsed.svg?longCache=True)](https://pypi.org/project/elapsed/)
[![](https://img.shields.io/pypi/v/elapsed.svg?maxAge=3600)](https://pypi.org/project/elapsed/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/elapsed.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/elapsed.py/)

#### Installation
```bash
$ [sudo] pip install elapsed
```

#### Features
+   accepts `datetime` or pid. `os.getcwd()` by default

#### Classes
class|`__doc__`
-|-
`elapsed.Elapsed` |

#### Functions
function|`__doc__`
-|-
`elapsed.days(input=None)` |return elapsed time in days. accepts pid or datetime
`elapsed.get(input=None)` |return elapsed.Elapsed instance. accepts pid or datetime
`elapsed.hours(input=None)` |return elapsed time in hours. accepts pid or datetime
`elapsed.minutes(input=None)` |return elapsed time in minutes. accepts pid or datetime
`elapsed.seconds(input=None)` |return elapsed time in seconds. accepts pid or datetime

#### Examples
`datetime` elapsed time
```python
>>> dt = datetime.datetime.now()
>>> time.sleep(2)
>>> elapsed.get(dt)
'00:02'
```

process  elapsed time by pid (`os.getpid()` by default)
```python
>>> import elapsed
>>> e = elapsed.get(1)
'02-16:30:38'
>>> e.days, e.hours, e.minutes, e.seconds
(2, 64, 3870, 232238)
```

`elapsed.seconds()`, `elapsed.minutes()`, `elapsed.hours()`, `elapsed.days()`
```python
>>> elapsed.seconds(1)
232238
>>> elapsed.minutes(1)
3870
>>> elapsed.hours(1)
64
>>> elapsed.days(1)
2
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>