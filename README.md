# git-tar

기타 악보 및 타브 모음.

## Requirements

- Python 3.12+
- [mise](https://mise.jdx.dev/) (recommended for version management)

## Setup

```bash
# Install mise (if not already installed)
curl https://mise.run | sh

# Install dependencies
mise install\nuv sync
```

## Development

```bash
uv run python -m git_tar.main
```

## Testing

```bash
uv run pytest
```

## Project Structure

```
git-tar/
├── src/
│   └── git_tar/
│       ├── __init__.py
│       └── main.py
├── tests/
├── pyproject.toml
├── README.md
└── CLAUDE.md
```

## License

This project is licensed under the NO LICENSE License.
