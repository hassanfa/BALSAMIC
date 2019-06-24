import BALSAMIC


def test_cli(invoke_cli):
    # GIVEN I want to see version of the program
    # WHEN I am asking to see version
    result = invoke_cli(['--version'])

    # THEN It should show the version of the program
    assert BALSAMIC.__version__ in result.output


def test_config(invoke_cli):
    # GIVEN I want to see config command options
    # WHEN asking to show config options
    result = invoke_cli(['config'])

    # THEN It should show config options in result
    assert 'sample' in result.output
    assert 'report' in result.output


def test_sample(invoke_cli):
    # GIVEN want to see config-sample params with help option
    # WHEN asking to show params for config-sample
    result = invoke_cli(['config', 'sample', '--help'])

    # THEN It should show all params reuired for config-sample
    assert 'sample-id' in result.output
    assert result.exit_code == 0


def test_sample_missing_opt(invoke_cli):
    # WHEN invoking command with missing options
    result = invoke_cli(['config', 'sample'])

    # THEN It should throw missiong option error
    assert 'Error: Missing option' in result.output
    assert result.exit_code == 2


def test_install(invoke_cli):
    # WHEN invoking install command with help option
    result = invoke_cli(['install', '--help'])

    # THEN It should list all the params without error
    assert result.exit_code == 0
    assert '--input-conda-yaml' in result.output


def test_install_missing_opt(invoke_cli):
    # WHEN invoking install command with missing option
    result = invoke_cli(['install'])

    # THEN It should esclate the missing option error
    assert 'Error: Missing option' in result.output
    assert result.exit_code == 2


def test_install_invalid(invoke_cli):
    # GIVEN wrong wrong env type, '-t' should have 'P','D','S'.
    # WHEN invoking command with invalid input
    result = invoke_cli(['install', '-t', 'foo'])

    # THEN It should throw invalid input error
    assert result.exit_code == 2
    assert 'Error: Invalid value' in result.output


def test_run(invoke_cli):
    # WHEN asking to options for run command
    result = invoke_cli(['run', '--help'])

    # THEN It should show all the params without any error
    assert result.exit_code == 0
    assert "--analysis-type" in result.output
    assert "--snake-file" in result.output
    assert "--sample-config" in result.output
    assert "--run-mode" in result.output
    assert "--cluster-config" in result.output
    assert "--run-analysis" in result.output


def test_run_missing_opt(invoke_cli):
    # WHEN invoking run command with missing option
    result = invoke_cli(['run'])

    # THEN It should throw missiong option error
    assert 'Error: Missing option' in result.output
    assert result.exit_code == 2


def test_run_invalid(invoke_cli):
    # WHEN invoking run with invalid input value
    result = invoke_cli(['run', '--run-mode', 'foo'])

    # THEN It should throw invalid value error
    assert result.exit_code == 2
    assert 'Error: Invalid value' in result.output


def test_initiate(invoke_cli):
    # GIVEN initiate subcommand
    # WHEN invoking initiate subcommand
    result = invoke_cli(['initiate'])

    # THEN It should show config options in result
    assert 'reference' in result.output
    assert result.exit_code == 0


def test_initiate_reference(invoke_cli):
    # GIVEN initiate reference subcommand
    # WHEN invoking initiate reference subcommand
    result = invoke_cli(['initiate', 'reference', '--help'])

    # THEN It should show config options in result
    assert '--output-dir' in result.output
    assert '--output-config' in result.output
    assert result.exit_code == 0


def test_initiate_reference_missing_opt(invoke_cli):
    # GIVEN initiate reference subcommand
    # WHEN invoking initiate reference subcommand
    result = invoke_cli(['initiate', 'reference'])

    # THEN It should show config options in result
    assert 'Error: Missing option ' in result.output
    assert result.exit_code == 2
