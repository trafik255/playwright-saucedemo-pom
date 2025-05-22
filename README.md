
# Playwright POM Test Framework for SauceDemo

![Playwright Tests](https://github.com/trafik255/playwright-saucedemo-pom/actions/workflows/playwright.yml/badge.svg)

## 🌟 About This Project

This project is a UI test automation framework built using Python, designed to demonstrate best practices in web application testing. It leverages Microsoft Playwright for robust browser interaction and Pytest for efficient test execution and management. The framework is structured using the Page Object Model (POM) design pattern, promoting maintainable and scalable test suites.

It includes a comprehensive suite of example tests for [SauceDemo](https://www.saucedemo.com), a sample e-commerce application, covering typical user flows such as login, product browsing, adding items to the cart, and the checkout process. The project is also configured for Continuous Integration (CI) using GitHub Actions, with automated tests running on every push and pull request, as indicated by the status badge above.

---

## 📁 Project Structure

Here's a breakdown of the main directories and key files in this project:

*   **`pages/`**: This directory contains the Page Object Model (POM) classes. Each file (e.g., `login_page.py`, `inventory_page.py`, `cart_page.py`) corresponds to a specific page in the SauceDemo web application and encapsulates the locators and actions for web elements on that page.

*   **`tests/`**: This directory houses all the test scripts written using Pytest. Test files (e.g., `test_login.py`, `test_inventory.py`, `test_checkout_flow.py`) use the page objects from the `pages/` directory to interact with the application and verify its behavior.

*   **`.github/workflows/`**: This directory contains GitHub Actions workflow configurations.
    *   `playwright.yml`: Defines the CI/CD pipeline that automatically runs the Playwright tests on events like pushes or pull requests to the repository.

*   **`requirements.txt`**: This file lists all the Python dependencies required to run the project (e.g., `playwright`, `pytest`). These can be installed using `pip install -r requirements.txt`.

*   **`pytest.ini`**: This is the configuration file for Pytest. It can be used to customize test discovery, markers, and other Pytest behaviors.

*   **`README.md`**: (This file) Provides a comprehensive overview of the project, including setup instructions, project structure, and how to run tests.

---

## 🚀 Project Setup and Execution

### Prerequisites

*   Python 3.7+
*   pip (Python package installer)

### 1. Clone the Repo

```bash
git clone https://github.com/trafik255/playwright-saucedemo-pom.git
cd playwright-saucedemo-pom
```
### 2. Set Up Python Environment

Create and activate a virtual environment:

*   **macOS/Linux:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
*   **Windows:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

Install dependencies:
```bash
pip install -r requirements.txt
```

Install Playwright browsers:
```bash
playwright install
```

### 3. Running Tests

To run all tests:
```bash
pytest
```

To run tests in a specific file:
```bash
pytest tests/test_login.py
```

To run tests matching a keyword expression:
```bash
pytest -k "add_to_cart"
```

For more options, refer to the [Pytest documentation](https://docs.pytest.org/en/stable/usage.html).

### 4. Test Suite Overview

This test suite aims to cover the primary user functionalities of the SauceDemo application.

**Key Scenarios Tested:**

*   **Login:**
    *   Successful login with valid credentials (`standard_user`).
    *   Verification of error messages for invalid credentials (e.g., `locked_out_user`, incorrect passwords).
*   **Inventory Management:**
    *   Verification that the product list is displayed after login.
    *   Adding and removing items from the cart directly from the inventory page.
    *   Sorting products by different criteria (e.g., name, price).
*   **Shopping Cart:**
    *   Verification that items added to the cart are correctly displayed.
    *   Removing items from the cart.
    *   Proceeding to checkout.
*   **Checkout Process:**
    *   Filling in user information (first name, last name, zip code).
    *   Verifying the order summary.
    *   Completing the purchase and verifying the "Thank you" message.
*   **Burger Menu Navigation:** (If tests for this exist or are planned, good to mention)
    *   Logging out of the application.
    *   Accessing the "About" page.
    *   Resetting the application state.

**Test Users (provided by SauceDemo):**

The following user credentials are used in the tests:

*   **Standard User:**
    *   Username: `standard_user`
    *   Password: `secret_sauce`
    *   Description: Standard access to all site features.
*   **Locked Out User:**
    *   Username: `locked_out_user`
    *   Password: `secret_sauce`
    *   Description: Used to test login error messages.
*   **Problem User:**
    *   Username: `problem_user`
    *   Password: `secret_sauce`
    *   Description: Used to test scenarios where product images/functionality might be incorrect.
*   **Performance Glitch User:**
    *   Username: `performance_glitch_user`
    *   Password: `secret_sauce`
    *   Description: Used to test application behavior under simulated performance delays.

More test user details can be found on the [SauceDemo website](https://www.saucedemo.com/).