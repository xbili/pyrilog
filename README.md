# Pyrilog

Generate a Wallace Partial Product Reduction Tree (PPRT) in Verilog. Fully
written in Python.

## Installation

Pyrilog is hosted on PyPI.

`pip install pyrilog`

## Usage

`pyrilog -k <operands> -w <width> -n <module name> -o <file directory>`

### Arguments

* `<operands>` represents the number of inputs you want the tree to accomodate.
* `<width>` represents the bit width of each input.
* `<module name>` represents the what you want to call the Verilog module.
* `<file directory>` is where you want the generated Verilog files to be placed.
