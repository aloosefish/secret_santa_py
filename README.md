## TODO
* Write tests that check that responses to external services come back correct.
* completely remove any API keys that might have been committed.


## Secret Santa py

[![codecov](https://codecov.io/github/aloosefish/secret_santa_py/branch/master/graph/badge.svg?token=7G5QUF6DIK)](https://codecov.io/github/aloosefish/secret_santa_py)

This program assigns every contact a unique Secret Santa.
It then sends each contact a text message with the name of 
their Secret Santa (from "Robot Santa"). It can be 
run automatically on a designated date (using the included [GitHub Action](https://github.com/aloosefish/secret_santa_py/blob/1a5bcac84892bd31f78a09c14d07bac44b233fa3/.github/workflows/create_and_send_on_schedule.yml)) or 
manually.

### Here are the rules:

* Need at least 8 contacts
* You cannot be your own Secret Santa.
* Your spouse (if you have one) cannot be your Secret Santa.
* You cannot have or be multiple people's Secret Santa.

### Tech

This project was built with the following tools:

* [Sendgrid](https://www.sendgrid.com/) for sending emails
* [jsonbin.io](https://jsonbin.io) for simple, private JSON storage and
  retrieval.
* [faker](https://faker.readthedocs.io/en/master/) for generating test data.
* [pytest](https://docs.pytest.org/) for writing and running tests.
* [GitHub Actions](https://docs.github.com/en/actions) for running script on 
  a given date and time

### How to run

- `poetry build` to build distributable archives
- `poetry run pytest` : Tests that Secret Santa assignment algorithm works 
  correctly, with fake test data
- `poetry run python manual_run.py` : runs program manually
- `poetry run pytest --cov=src --cov-report=html` generate test coverage report

