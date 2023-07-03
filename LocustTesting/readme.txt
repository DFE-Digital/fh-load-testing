# fh-loadtesting
Contains all load tests for Family Hub suite of components

## Tools used
Tests are written in Locust https://docs.locust.io/en/stable/index.html

locust --host=https://localhost:7199 --run-time=60s --headless --users=10 --spawn-rate=1 --json




locust --host=https://test.find-support-for-your-family.education.gov.uk/ --run-time=60s --headless --users=10 --spawn-rate=1 --json