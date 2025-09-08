# Template Project

## Project structure
```bash
<project_name>/
├── README.md               # Project overview and instructions
├── config.yaml             # Configuration for model and features
├── poetry.lock             # Poetry lock file (dependencies)
├── pyproject.toml          # Project and dependency configuration
├── src/
└── __init__.py
```

## Installation

```bash
git clone https://github.com/<user>/<project>.git
cd <project>
pip install poetry
poetry env use python
poetry install
```

## Running scripts

Use Poetry to execute scripts:

```bash
poetry run python src/script.py
```

## Customization

- Update `pyproject.toml` with your project's metadata.
- Modify or add code under `src/` to suit your application.
- Adjust configurations such as `config.yaml` as needed.

