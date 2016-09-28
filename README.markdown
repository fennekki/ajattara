Ajattara
========

A tool and a library for measuring runtimes.

Runs a command batch as many times as specifed (default: 1000) in
batches of specified size (default: 10). Returns mean, median and
standard deviation of data.

Installation
------------

While in this directory, `pip install .`. Requires at least Python 3.4,
so use a Python 3 compatible pip.

Usage
-----

    Usage: ajattara [OPTIONS] COMMAND [ARG]...

      Measure runtime of a command. Return statistical data.
    
    Options:
      -s, --batch-size INTEGER        How many tests should be run per batch
      -b, --batches INTEGER           How many batches of tests to run
      --suppress-stdout / --no-suppress-stdout
                                      Redirect stdout from subprocesses to a byte
                                      sink.
      -o, --outfile PATH              Output run times to given file, one time per
                                      line
      --help                          Show this message and exit.
