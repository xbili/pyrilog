# Pyrilog

[![Build Status](https://travis-ci.com/xbili/pyrilog.svg?token=xyqyxbAevSn1zLgfHgcb&branch=master)](https://travis-ci.com/xbili/pyrilog)

Generates a Fused Multiply Add (FMA) unit in Verilog.

## Installation

`pip install pyrilog`

**NOTE: Currently not on PyPi yet - therefore the `pip` command would not work.**

Alternatively, you can clone this repository and run:

`python -m pyrilog <...args>`

## Usage

The Fused Multiply Add operation is in the form:

> `a + b * c`

However, in our case, we are not taking `a` as the accumulated value, but we
will keep `a` as an expanded value of the partial products so that  we can
perform the operation of a matrix dot product in a parallel
fashion.

`pyrilog --size <size> --width <width> --with-pipeline`


### Arguments

* `--size`: size of the vectors that we want to perform dot product on
* `--width`: bit width of each element in the vectors that we want to perform dot
product on
* `--with-pipeline`: we'll include latches in between the stages of the
reduction tree if this is enabled **(work in progress)**


## Verification

It is recommended that you test and verify the generated Verilog code using a
test bench with [Icarus Verilog](http://iverilog.icarus.com/) before deploying
to any hardware. Pyrilog does not provide generated Verilog code to run as a
test bench, although that would be pretty awesome.


## Documentation

Work-in-Progress. I'm hoping to use the GitHub wiki as the main source of
documentation.


## Development

If you are interested to contribute, feel free to take a look at the issues.
Feel free to clone this repository and make pull requests if you think there
are improvements to be made.

Clone the repository, create a `virtualenv` and run:

`pip install -r requirements.txt`


### Testing

Please remember to run tests before submitting a PR:

`nosetests ./tests/**/*.py --with-coverage`


### Python 3

Pyrilog is developed in a Python 3.6.2 environment, however there should be
support for lower versions of Python 3. I cannot guarantee support for Python
2 versions.
