import os
from enum import Flag
from typing import Final

import pytest
from envflag import EnvFlag

CASES: Final[list[tuple[str, bool]]] = [
    ("", False),
    ("1", True),
    ("0", False),
    ("True", True),
    ("TRUE", True),
    ("False", False),
    ("FALSE", False),
]


@pytest.mark.parametrize(("env_value", "expected"), CASES)
def test_should_return_correct_bool(env_value: str, expected: bool) -> None:
    # Given
    env_name = "TEST"
    os.environ[env_name] = env_value

    # When
    flag = EnvFlag(env_name)

    # Then
    assert flag.get() is expected


@pytest.mark.parametrize(("env_value", "expected"), CASES)
def test_should_return_correct_bool_as_descriptor(env_value: str, expected: bool) -> None:
    # Given
    env_name = "TEST"
    os.environ[env_name] = env_value

    class SomeEnum(Flag):
        TEST_FLAG = EnvFlag(env_name)

    # When & Then
    assert SomeEnum.TEST_FLAG is expected
