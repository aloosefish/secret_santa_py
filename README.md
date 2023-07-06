# TODO:

* write more, better tests
* run test automatically on every push to a PR 
  * confirming environment setup
* create package?

# Possible Enhancements:

* switch data store to TinyDB (
  using [this guide](https://www.pingcap.com/blog/how-to-deploy-tidb-on-google-cloud-platform-part-1/))
* make `contact_types.py` work with dot notations
* mock sending of text messages

## Secret Santa

This program assigns every contact a unique Secret Santa.
It then sends each contact a text message with the name of 
their Secret Santa via text message (from "Robot Santa"). The program is run 
automatically on a designated date and time.

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


- `poetry run pytest` : tests that everything works correctly, with 
  generated fake test data
- `poetry run python local_run.py` : runs program manually

