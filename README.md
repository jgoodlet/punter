# punter

[![status](https://img.shields.io/travis/jgoodlet/punter.svg)](https://travis-ci.org/jgoodlet/punter.svg)
[![version](http://img.shields.io/pypi/v/punter)](https://pypi.python.org/pypi/punter)
[![license](https://img.shields.io/pypi/l/punter.svg)](https://pypi.python.org/pypi/punter)

A tiny python wrapper for the Email Hunter API. Seriously. It's tiny.

## Usage

    >>> import punter
    >>> s = punter.search('d08d2ba22218d1b59df239d03fc5e66adfaec2b2', 'stripe.com')
    >>> s['status']
    u'success'
    >>> s['results']
    164
    >>> s['emails']
    [{
        "status": "success",
        "results": 164,
        "webmail": false,
        "pattern": "{first}"
        "offset": 0,
        "emails": [
            {
              "value": "hoon@stripe.com",
              "type": "personal",
              "sources": [
                {
                  "domain": "stripe.com",
                  "uri": "https://stripe.com/blog/weekly-and-monthly-transfers",
                  "extracted_on": "2015-03-05"
                }
              ]
            },
        ...
        ]
    }]

## Install

    $ pip install punter
