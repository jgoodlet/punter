# punter

[![status][1]][2]
[![version][3]][4]
[![license][5]][6]

A tiny python wrapper for the [Email Hunter API](https://emailhunter.co/api). Seriously. It's tiny.

## Usage

In most cases the primary usage will be executing searches on a domain. 

```python
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
```

Want to do an email search? Essentially the same deal.

```python
>>> import punter
>>> s = punter.search('d08d2ba22218d1b59df239d03fc5e66adfaec2b2', 'apple-pay@stripe.com')
>>> s['status']
u'success'
>>> s['exist']
True
>>> s['email']
u'apple-pay@stripe.com'
>>> s['emails']
[{
    u'domain': u'mpora.com', 
    u'extracted_on': u'2015-04-27', 
    u'uri': u'http://mpora.com/tags/wolfgang-wildner'
}]
```

## Install

```bash
$ pip install punter
```

## Todo

There's always room for improvement.

- More Pythonic!
- Tighten up the exception handling
- Tox configuration
- Perhaps make a cli (new project?)

## License

Copyright &copy; 2015 Joshua Goodlett

Released under the [MIT License (MIT)](https://github.com/jgoodlet/punter/blob/master/LICENSE)

[1]: https://img.shields.io/travis/jgoodlet/punter.svg
[2]: https://travis-ci.org/jgoodlet/punter.svg
[3]: https://img.shields.io/pypi/v/punter.svg
[4]: https://pypi.python.org/pypi/punter
[5]: https://img.shields.io/pypi/l/punter.svg
[6]: https://pypi.python.org/pypi/punter