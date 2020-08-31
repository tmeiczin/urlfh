# Description
Provides a file like IO handle for remote files over http(s). This differs from
urllib.urlopen() in that it will only fetch the data as requested per read. It
also supports seek, tell, and close allowing it be used in place of open().

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

You can use any Requests supported auth. Basic auth is supported by the urlopen function.

```
from urlfh import urlopen


fh = urlopen('http://example.com/demo.txt', username='bob', password='abc12345')
data = fh.read(20)
```

If you need different auth mechanisms you can use the UrlFh class and pass in any
Request auth object.
