# Pyrilog

Generate a Wallace Partial Product Reduction Tree (PPRT) in Verilog. Fully
written in Python.

## Installation

Pyrilog is hosted on PyPI.

`pip install pyrilog`

## Usage

`pyrilog -k <operands> -w <width> -n <module name> -o <file directory>`

### Arguments

* `<inputs>` represents the number of inputs you want the tree to accomodate.
* `<bits>` represents the number of bits each input has.
* `<file directory>` is where you want the generated Verilog files to be placed.
