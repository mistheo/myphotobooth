run:
    uv run python -m src.myphotobooth
test:
    uv run pytest -v
lint:
    uv run ruff check src tests
