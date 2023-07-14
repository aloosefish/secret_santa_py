## Secret Santa py

[![codecov](https://codecov.io/github/aloosefish/secret_santa_py/branch/master/graph/badge.svg?token=7G5QUF6DIK)](https://codecov.io/github/aloosefish/secret_santa_py)

This program assigns every contact a unique Secret Santa.
It then sends each contact a text message with the name of 
their Secret Santa via text message (from "Robot Santa"). The program can be 
run automatically on a designated date and time or manually.



### Here are the rules:

* Need at least 8 contacts
* You cannot be your own Secret Santa.
* Your spouse (if you have one) cannot be your Secret Santa.
* You cannot have or be multiple people's Secret Santa.

### Tech

This project was built with the following tools:

* [Twilio](https://www.twilio.com/) for sending text messages
* [jsonbin.io](https://jsonbin.io) for simple, private JSON storage and
  retrieval
* [faker](https://faker.readthedocs.io/en/master/) for generating test data
* [pytest](https://docs.pytest.org/) for writing and running tests
* [GitHub Actions](https://docs.github.com/en/actions) for automatically sending
  messages on a certain date and time

# Possible Future Enhancements:

* more efficient Secret Santa assignment algorithm
* a front end for uploading contacts
* make `contact_types.py` with different data types
* mock sending of text messages

# How to run

- `poetry build` to build distributable archives
- `poetry run pytest` : Tests that Secret Santa assignment algorithm works 
  correctly, with generated fake test data
- `poetry run python manual_run.py` : runs program manually
- `poetry run pytest --cov=src --cov-report=html` generate test coverage report

