#!/usr/bin/env python

"""Tests for `melt_to_gephi` package."""


import unittest
from click.testing import CliRunner

from melt_to_gephi import melt_to_gephi
from melt_to_gephi import cli


class TestMelt_to_gephi(unittest.TestCase):
    """Tests for `melt_to_gephi` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'melt_to_gephi.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
