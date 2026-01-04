import pytest

from ec_gen.skeleton import fib, main, run

__author__ = "Wai-Shing Luk"
__copyright__ = "Wai-Shing Luk"
__license__ = "MIT"


def test_fib() -> None:
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys: pytest.CaptureFixture) -> None:
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["7"])
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out


def test_main_with_no_args(capsys: pytest.CaptureFixture) -> None:
    """Test main function with no arguments"""
    import sys
    from io import StringIO

    # Redirect stderr to capture error messages
    old_stderr = sys.stderr
    sys.stderr = StringIO()

    try:
        with pytest.raises(SystemExit):
            main([])
    finally:
        # Restore stderr
        error_output = sys.stderr.getvalue()
        sys.stderr = old_stderr

    # Check that it handles no arguments with an error
    assert "error" in error_output.lower() or "required" in error_output.lower()


def test_run(capsys: pytest.CaptureFixture) -> None:
    """Test run function which calls main with sys.argv"""
    import sys

    # Save original argv
    original_argv = sys.argv

    try:
        # Mock sys.argv[1:] to simulate command line arguments
        sys.argv = ["skeleton.py", "7"]
        run()
        captured = capsys.readouterr()
        assert "The 7-th Fibonacci number is 13" in captured.out
    finally:
        # Restore original argv
        sys.argv = original_argv
