[![Build Status](https://travis-ci.com/otahontas/tuho.svg?branch=master)](https://travis-ci.com/otahontas/tuho)
## Local usage

   * Create virtual environment `python3 -m venv venv`
   * Activate virtual environment `source venv/bin/activate`
   * Upgrade pip `pip install --upgrade pip`
   * Install project dependencies `pip install -r requirements.txt`
   * Run the application `python3 run.py`
   * Use a web browser to navigate to `localhost:5000`

## Demo
- App [runs on heroku](https://tuho-lukuvinkkikirjasto.herokuapp.com/) (you may have to wait for a short while before app starts)

## Code style

Code style should follow style guides described in [pep8](https://www.python.org/dev/peps/pep-0008/). Linting can be done with flake8 (installed to venv) and imports can be sorted with isort.


## Definition of done
- User story specified and accepted by product owner
- Feature planned
- Feature implemented
- Automatic tests implemented and passed
- Feature integrated to rest of the software
- Feature documented

## Git commit style
- Git commits should use style spesified in [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

## Testing
- Repo includes ready-to-use database for testing. Keep your modified test database version in .gitignore, don't override master in repo.
- **Travis link should be added here**

## Product and sprint backlogs
- Markdown-styled product backlog [can be found here](https://github.com/otahontas/tuho/blob/master/documentation/productbacklog.md)
- Sprint backlogs can be found behind [Projects-tab](https://github.com/otahontas/tuho/projects)
- Sprint working hours and burndown chart in [Google Drive](https://docs.google.com/spreadsheets/d/1mZTxDfF5NAi7l06G1bbRIsrdH6kzyGXTUGnV5ptv-mw/edit?usp=sharing)
