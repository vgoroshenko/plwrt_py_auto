[![Test and Deploy result from Python](https://github.com/vgoroshenko/plwrt_py_auto/actions/workflows/py_env.yml/badge.svg?branch=main)](https://github.com/vgoroshenko/plwrt_py_auto/actions/workflows/py_env.yml)
## Playwright Pytest Allure Page object model example 


[Example application for writing automated acceptance tests](http://the-internet.herokuapp.com)

[Link to Allure report after run tests](https://vgoroshenko.github.io/plwrt_py_auto)

Install your dependencies:

    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    playwright install --with-deps

Start web server:

    docker-compose up -d

Load the page you want to see in your browser:

    http://localhost:5000/

Start tests (run parallel tests in 3 browser):

    pytest

See Allure report result:
    
    allure serve reports

Start tests using Docker test:

    docker run -v .:/app vgoroshenko/playwright sh -c "pip install  -r requirements.txt; pytest"
    docker run -v .:/app vgoroshenko/allure sh -c "allure generate reports"


An example application that captures prominent and ugly functionality found on the web. Perfect for writing automated acceptance tests against.

Deployed and available at [http://the-internet.herokuapp.com](http://the-internet.herokuapp.com).