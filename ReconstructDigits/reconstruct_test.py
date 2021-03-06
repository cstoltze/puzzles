import pytest

from reconstruct import reconstruct


@pytest.mark.parametrize(
    "test_input,expected",
    [
        pytest.param("owoztneoer", "012"),
        pytest.param("fviefuro", "45"),
        pytest.param("zerozerozero", "000"),
        pytest.param("sevenonezero", "017", id="recursive, one has no unique_chars"),
    ],
)
def test_reconstruct(test_input, expected):
    assert reconstruct(test_input) == expected
