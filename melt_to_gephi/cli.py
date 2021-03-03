"""Console script for melt_to_gephi."""
import sys
import click


@click.command()
@click.option('--files',default = './data',
            help='This is the Folder path with the rawfiles')

@click.option('--filename',default='gephi_ready_file',
            help='assign filename to the gephi ready file')

def main():
    """This is the Console script for melt_to_gephi.
    """
    click.echo("use 'melt_to_gephi --help' to see options")
    click.echo("See documentation at https://melt-to-gephi.readthedocs.io/en/latest/installation.html")
    return 0
# def cli(files):
#     """Refers to a Folder path with the rawfiles
#     """
#     click.echo("use 'melt_to_gephi --help' to see options" % files)
#     return 0

#
if __name__ == "__main__":
    main()  # pragma: no cover
