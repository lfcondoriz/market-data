# Market Data Platform

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver

## Installation

### 1. Install uv

```bash
# On macOS or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy BypassUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### 2. Clone and setup the project

```bash
git clone <your-repo-url>
cd market-data
```

### 3. Install dependencies

```bash
uv sync
```

This will:
- Create a virtual environment (`.venv`)
- Install all dependencies
- Set up the project in editable mode

## Usage

### Run the application

```bash
uv run market-data
```

### Run a Python script

```bash
uv run src/market_data/some_script.py
```

### Add new dependencies

```bash
uv add package-name
```

Example:
```bash
uv add requests pandas
```

### Update dependencies

```bash
uv sync --upgrade
```

### Activate virtual environment (optional)

```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## Development

### Run the project in development mode

```bash
uv run market-data
```

### Install development dependencies

```bash
uv add --dev pytest ruff
```

### Code Quality

#### Ruff
To run Ruff for linting and formatting:

```bash
# Check for linting issues
uv run ruff check src/market_data

# Fix linting issues automatically
uv run ruff check . --fix

# Format code
uv run ruff format .
```

## Learn more

- [uv Documentation](https://docs.astral.sh/uv/)
- [Python Packaging Guide](https://packaging.python.org/)
