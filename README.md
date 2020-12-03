<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/elapsed.svg?maxAge=3600)](https://pypi.org/project/elapsed/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/elapsed.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/elapsed.py/actions)

### Installation
```bash
$ [sudo] pip install elapsed
```

#### Features
+   accepts `datetime` or pid. `os.getcwd()` by default

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
