import pytest

import BALSAMIC
from BALSAMIC.commands.base import cli

def test_deliver(invoke_cli, tumor_only_config):
    # GIVEN a tumor-normal config file
    # WHEN running analysis
    result = invoke_cli(['plugins', 'deliver', '--sample-config', tumor_only_config])

    # THEN it should run without any error
    assert result.exit_code == 0