# QP Site - CI/CD with Jenkins

This repository includes automated testing and CI/CD using Jenkins.

## Running Tests Locally

Install dependencies:
```bash
pip install -r requirements.txt
```

Run tests:
```bash
python -m pytest tests/ --verbose
```

Run tests with coverage:
```bash
python -m pytest tests/ --cov=. --cov-report=html
```

## Jenkins Pipeline

The `Jenkinsfile` defines a CI/CD pipeline with the following stages:

1. **Checkout** - Pull latest code from repository
2. **Setup** - Install Python dependencies
3. **Run Tests** - Execute unit tests with pytest
4. **Test Report** - Publish JUnit test results
5. **Deploy** - Deploy to GitHub Pages (automatic via git push)

### Setting up Jenkins

1. Install Jenkins and required plugins:
   - Pipeline plugin
   - Git plugin
   - JUnit plugin
   - Python plugin (optional)

2. Create a new Pipeline job in Jenkins
3. Point to this repository
4. Jenkins will automatically detect the `Jenkinsfile`

### Test Structure

```
tests/
├── __init__.py
└── test_utils.py       # Sample unit tests
```

## GitHub Pages Deployment

The site is automatically deployed to GitHub Pages when you push to the `main` branch:
- URL: https://kkalaivani-glitch.github.io/DrKK-QP/

## Files

- `Jenkinsfile` - Jenkins pipeline configuration
- `requirements.txt` - Python testing dependencies
- `tests/` - Unit test directory
- `index.html` - Main question paper page
