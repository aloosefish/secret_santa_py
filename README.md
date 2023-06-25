# TODO:
* ~~figure out packaging/dependencies, with Poetry~~
* create data structure for contacts
* generate test data and write tests first? including mock sending text 
  messages?
* implement efficient combination algorithm


## Secret Santa

This program assigns everyone in a contacts json file a unique Secret Santa
then sends each contact a text message with the name and phone number of their
Secret Santa via text message (from "Robot Santa").

### Here are the rules:

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
  messages on a certain day

### How to set up this project for your own use 
_(do I really care about making this usable for others? maybe do 'how this 
works' instead)_

1) Clone this repo.
2) Create a twilio account and purchase a phone number.
3) Create a jsbin.io account
4) Put the participants in your Secret Santa pool into a JSON file with the
   following schema --- and upload it to jsbin.io.

### How this works
1) JSON data is pulled from jsonbin.io
2)


- `pytest run test` : tests that everything works correctly
- `python3 main.py` : runs program manually

