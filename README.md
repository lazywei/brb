BRB: Be Right Back
===================

BRB is a python package that helps you cache your functions with customizability.


## Install

```
pip install brb
```

## Usage

```python
import brb

def foo(bar, baz):
    print('bar={}, baz={}'.format(bar, baz))
    return ', '.join(bar, baz)
    
brb.cache(foo, maxsize=128)("Loo", "Foo")
```

## LICENSE

MIT
