## Getting Started Playwright tests the Internet project

Install your dependencies:

    make pull
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    playwright install chrome

Start selenoid server:

    docker-compose up -d

Load the page you want to see in your browser:

    http://localhost:5000/

Start tests:

    pytest -s -v --tb=line  --browser-channel chrome --headed -n 5 -q --alluredir=reports
    pytest -s -v --tb=line --screenshot=on --browser webkit --browser firefox --browser chromium -n 5
    pytest -s -v --tb=line --headed --screenshot=on


An example application that captures prominent and ugly functionality found on the web. Perfect for writing automated acceptance tests against.

Deployed and available at [http://the-internet.herokuapp.com](http://the-internet.herokuapp.com).