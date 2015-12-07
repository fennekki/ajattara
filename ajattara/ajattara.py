import subprocess
from time import time
from os import devnull
from statistics import mean, median, stdev

import click


class Ajattara(object):
    """A class for measuring runtimes of things"""

    def __init__(self, batch_count, batch_size, function, args=[], kwargs={}):
        """Initialise an object.

        Params:
            function (function): The function to be run and measured
            batch_count (int): The amount of batches to run
            batch_size (int): The number of runs per batch
        """
        self.__function = function
        self.__args = args
        self.__kwargs = kwargs
        self.__batch_count = batch_count
        self.__batch_size = batch_size

    def run(self):
        """Run the function a specified amount of times."""
        returns = []
        for i in range(self.__batch_count):
            start = time()
            for _ in range(self.__batch_size):
                self.__function(*self.__args, **self.__kwargs)
            stop = time()
            returns.append(stop - start)
        return returns


@click.command(help="Measure runtime of a command. "
                    "Return statistical data.")
@click.option("-s", "--batch-size", default=10,
              help="How many tests should be run per batch")
@click.option("-b", "--batches", default=1000,
              help="How many batches of tests to run")
@click.option("--suppress-stdout/--no-suppress-stdout", default=True,
              help="Redirect stdout from subprocesses to a byte sink.")
@click.argument("command")
@click.argument("arg", nargs=-1)
def run_program(batch_size, batches, command, suppress_stdout, arg):
    """Run a command given on the command line.

    Arguments are parsed from the following list.
    """
    # Generate argument list for Popen
    arguments = [command]
    arguments.extend(arg)

    with open(devnull, "w") as nullfile:
        if not suppress_stdout:
            progr_stdout = None
        else:
            progr_stdout = nullfile
        a = Ajattara(batch_count=batches, batch_size=batch_size,
                     function=subprocess.call,
                     kwargs={"args": arguments, "stdout": progr_stdout})
        # Run and do analysis
        results = a.run()
        click.echo("{} batches of {} runs".format(batches, batch_size))
        click.echo("mean {}s median {}s standard deviation {}"
                   .format(mean(results), median(results), stdev(results)))
