# UrlFH
## File like IO handle for remote files over http

# Installation

```
pip install urlfh
```

# Getting Started

The remote http server must support ranges. 

```
from urlfh import urlopen


fh = urlopen('http://example.com/demo.txt')
data = fh.read(20)
fh.seek(0)
data = fh.read(20)
```

Alternatively, you can use the with context

```
from urlfh import urlopen

with urlopena'http://example.com/demo.txt') as fh:
    data = fh.read(20)
```

In some cases, a server may support ranges, but does not include the range header. In this case, you can disable the check.

```
from urlfh import urlopen


fh = urlopen('http://example.com/demo.txt', ensure_range_headers=False)
data = fh.read(20)
```
