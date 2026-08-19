# MiniMart

MiniMart is a small online shop that we will build one step at a time. Visitors will eventually browse and search for products. Customers will use a cart and place simulated orders, while administrators will manage products and view reports. No real payments will be taken.

## Final folder structure

Some of these files will be added in later milestones. We do not create empty application files before they are needed.

```text
minimart/
├── app.py
├── config.py
├── database.py
├── schema.sql
├── seed.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── prompts/
│   └── prompt-log.md
├── docs/
├── tests/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
└── templates/
    ├── base.html
    ├── index.html
    ├── products.html
    ├── product-detail.html
    ├── login.html
    ├── register.html
    ├── cart.html
    ├── orders.html
    ├── admin-products.html
    └── cost-report.html
```

## Software installation requirements

Install these tools before starting:

- Python 3.11 or newer
- `pip`, which normally comes with Python
- Git
- A code editor and a web browser
- A GitHub account (needed in a later module)

SQLite support is included with Python, so it does not need a separate installation.

## Setup commands

Open a terminal in the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1` instead. Then visit <http://127.0.0.1:5000/>. Stop the server with **Ctrl+C**.

## Course milestones

1. Create a Flask home page with a reusable Bootstrap template.
2. Review the prototype and add the product catalogue and SQLite schema.
3. Review AI-generated code in small, understandable changes.
4. Add registration, login, password hashing, and role-based access control.
5. Move configuration and secrets into environment variables.
6. Add OWASP-aligned validation and security tests.
7. Practise Git commits and record important prompts.
8. Add GitHub Actions for automated checks.
9. Add unit, integration, and edge-case tests with coverage.
10. Add safe application logging and optional monitoring.
11. Document deployment, backup, and rollback steps.
12. Add the administrator cost-price report and discuss cost and ROI.

## Risks we will address later

- **Password theft:** hash passwords and never log them.
- **Unauthorised access:** check customer and administrator permissions in Flask routes.
- **SQL injection:** use parameterised SQLite queries for all user-provided values.
- **Cross-site scripting:** validate input and let Jinja escape displayed values.
- **Cross-site request forgery:** protect actions that change data.
- **Session attacks:** use a secret key from the environment and secure cookie settings.
- **Stock mistakes:** verify stock during checkout and update it safely.
- **Price tampering:** calculate totals on the server rather than trusting the browser.
- **Information leaks:** keep cost prices, error details, and secrets away from public pages and logs.
- **Data loss:** plan database backups, deployment checks, and rollbacks.
- **Broken changes:** use automated tests and continuous integration before deployment.
- **Dependency problems:** pin, review, and update dependencies carefully.
- **Monitoring gaps:** add useful logs without recording passwords, cookies, keys, or tokens.

## Milestone 1: Flask home page

This first milestone deliberately stays small.

### What each file does

- `app.py` creates the Flask application. Its `/` route renders the home page.
- `templates/base.html` holds the shared HTML page and loads Bootstrap 5.
- `templates/index.html` supplies the content for the home page.
- `requirements.txt` tells `pip` which Flask version to install.
- `prompts/prompt-log.md` records the important prompt and proposed change.

Flask uses Jinja templates. The home template *extends* the base template, which means future pages can reuse the same navigation and layout.

### Test checklist

- [ ] The virtual environment is active.
- [ ] `python -m pip install -r requirements.txt` finishes without an error.
- [ ] `python app.py` starts the development server.
- [ ] <http://127.0.0.1:5000/> shows “Welcome to MiniMart”.
- [ ] The page has a blue MiniMart navigation bar and a light welcome panel.
- [ ] The terminal does not show an error when the page loads.

Stop here after testing. Review the proposed change in `prompts/prompt-log.md`, then say **continue** when you are ready for the next milestone.
