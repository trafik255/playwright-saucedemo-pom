
# Playwright POM Test Framework for SauceDemo

![Playwright Tests](https://github.com/trafik255/playwright-saucedemo-pom/actions/workflows/playwright.yml/badge.svg)


This project uses [Microsoft Playwright](https://playwright.dev/python/) and Pytest to automate end-to-end UI testing of [SauceDemo](https://www.saucedemo.com), a sample e-commerce site for automation practice. It is structured using the Page Object Model (POM) design pattern.

---

## 📁 Project Structure


---

## 🚀 Getting Started

### 1. Clone the Repo

```
git clone https://github.com/YOUR_USERNAME/playwright-saucedemo-pom.git
cd playwright-saucedemo-pom
```
### 2. Set Up Python Environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```
### 3. Running Tests
To run all tests:
```
pytest
```
Run a specific test:
```
pytest tests/test_login.py

```
### 🧪 What It Tests
Login using standard_user and secret_sauce
Assert that the inventory page is displayed
Verifies product list is visible

### 🛠️ Test Users (provided by SauceDemo)
✅ Username: standard_user
✅ Password: secret_sauce
More test users at: https://www.saucedemo.com/