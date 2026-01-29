"""Test main module."""

from git_tar.main import main


def test_main(capsys):
    """Test main function."""
    main()
    captured = capsys.readouterr()
    assert "Hello" in captured.out
