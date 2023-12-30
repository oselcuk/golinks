# golinks

Very barebones golinks implementation. All HTML/CSS written with copilot and google-fu, so user beware.

Still to do:

* Add owners list, only allow managing by owners
* Split creation and modification flows
* Use postgres instead of sqlite
* Add tests
* Make prettier?

## Running

Install in a venv with `pip install -e .`, run migrations with `manage migrate` and run locally with `manage runserver`.

## Usage

Go to `localhost:8000` to see existing golinks.

Go to `localhost:8000/name` to be redirected to the URL saved with that name. If there isn't one, you'll be taken to a screen to create that golink.