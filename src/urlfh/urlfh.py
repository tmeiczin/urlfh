# -*- coding: utf-8 -*-

"""
urlfh
~~~~~~~~~~~~~~~~

This module provides file handle functionality of a resource over http
on servers that accept ranges. The method urlopen handles basic auth
and other auth mechanisms support by requests can be passed into the class.

>>> import urlfh
>>> urlfh.open(path)
"""

import os
import requests


def urlopen(path, username=None, password=None, enforce_range_headers=True):
    auth = None
    if path.startswith('http'):
        if username:
            auth = request.auth.HTTPBasicAuth(username, password)
        return UrlFH(path, auth=auth, enforce_range_headers=enforce_range_headers)
    else:
        return open(path, 'rb')


class UrlFH(object):
    """
    This class provides file handle functionality of a resource over http
    on servers that accept ranges.
    """
    def __init__(self, url, auth=None, enforce_range_headers=True):
        """
        Create a file like handle from a URL.

        :param str url:    The resource URL
        :return:           Url filehandlee
        """
        self.url = url
        self.auth = auth
        self.name = os.path.basename(url)
        result = requests.head(url, auth=self.auth)

        if not result.status_code // 100 == 2:
            raise IOError('could not connect to server')

        if 'accept-ranges' not in result.headers and enforce_range_headers:
            raise IOError('server does not support accept ranges')

        self.size = int(result.headers['Content-length'])
        self.offset = 0

    def tell(self):
        return self.offset

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.offset = min(max(offset, 0), self.size)
        elif whence == os.SEEK_CUR:
            if offset < 0:
                self.offset = max(self.offset + offset, 0)
            else:
                self.offset = min(self.offset + offset, self.size)
        elif whence == os.SEEK_END:
            self.offset = (max(min(self.size + offset, self.size), 0))

        return self.offset

    def seekable(self):
        return True

    def read(self, size=None):
        if size is None:
            size = self.size - self.offset

        start = self.offset
        end = start + size - 1

        headers = {
            'Range': 'bytes=%s-%s' % (start, end)
        }
        request = requests.get(self.url, auth=self.auth, headers=headers)
        self.offset += size

        if request.status_code // 100 == 2:
            return request.content

        return ''

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass
