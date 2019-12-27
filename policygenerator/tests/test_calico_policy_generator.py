#!/usr/bin/env python

"""Tests for `policy_generator` package."""

import pytest

from click.testing import CliRunner
from policy_generator import calico_policy_generator

def test_generate_calico_policy():
    runner = CliRunner()
    result = runner.invoke(calico_policy_generator.generate_calico_policy, ['--policydata', 'tests/data-good.yaml'])
    assert result.exit_code == 0
    result = runner.invoke(calico_policy_generator.generate_calico_policy, ['--policydata', 'tests/data-bad.yaml'])
    assert result.exit_code != 0
    result = runner.invoke(calico_policy_generator.generate_calico_policy, ['--policydata', 'tests/data1-good.yaml'])
    assert result.exit_code == 0
    result = runner.invoke(calico_policy_generator.generate_calico_policy, ['--policydata', 'tests/data1-bad.yaml'])
    assert result.exit_code != 0
