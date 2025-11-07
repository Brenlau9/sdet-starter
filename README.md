# SDET Starter: Pytest + CI + HTML Report

This is a **SDET starter** repository showing:
- Python unit tests with **pytest**
- **Parameterized** test cases and an **xfail** example
- **GitHub Actions** CI that runs tests on every push
- An **HTML test report** uploaded as an artifact

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest --html=report.html --self-contained-html
```

## Repo Structure

```
sdet-starter/
├─ src/
│  └─ text_utils.py
├─ tests/
│  └─ test_text_utils.py
├─ .github/workflows/ci.yml
├─ requirements.txt
├─ pytest.ini
└─ README.md
```

## GitHub Actions CI

The workflow:
- Sets up Python
- Installs dependencies
- Runs pytest with an HTML report
- Uploads the `report.html` as a build artifact
