## Getting Started Playwright tests the Internet project

[Example application for writing automated acceptance tests](http://the-internet.herokuapp.com)

[Link to Allure report after run tests](https://vgoroshenko.github.io/plwrt_py_auto)

Install your dependencies:

    make pull
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    playwright install

Start web server:

    docker-compose up -d

Load the page you want to see in your browser:

    http://localhost:5000/

Start tests:

    pytest -s -v --tb=line -n 5 --alluredir=reports -q     
    pytest -s -v --tb=line --browser webkit --browser firefox --browser chromium -n 5 --alluredir=reports -q  
    pytest -s -v --tb=line --headed


An example application that captures prominent and ugly functionality found on the web. Perfect for writing automated acceptance tests against.

Deployed and available at [http://the-internet.herokuapp.com](http://the-internet.herokuapp.com).