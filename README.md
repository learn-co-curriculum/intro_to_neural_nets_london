# Notebook Test Template

## What it does
Provides a framework to test variables and functions from student notebooks. Imports the notebook as a module, then uses pytest for the individual unit tests.

This is a [GitHub Template Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) so copying it is as easy as clicking the green "Use this Template" button on this repo page (https://github.com/learn-co-curriculum/dsc-notebook-test-template).

Copy the template and add your own test cases to your own repo.

## Initial Setup
* `pip install pytest`
* Run `pytest` from the root of this directory to see the examples run
* Should see something like (but with some colors!):

```
========================= test session starts ==========================
platform darwin -- Python 3.6.9, pytest-3.7.0, py-1.8.0, pluggy-0.12.0 -- /Users/alex/anaconda3/envs/learn-env/bin/python
cachedir: .pytest_cache
rootdir: /Users/alex/Development/DS/notebook_test_template, inifile: pytest.ini
collecting 0 items                                                     importing Jupyter notebook from index.ipynb





*****************
| Running Tests |
*****************


collected 4 items                                                      

test_grader.py::test_example
An example that will always pass
PASSED
test_grader.py::test_player_names
Create a list of all the keys in the players dictionary
PASSED
test_grader.py::test_player_nationalities
Create a list of tuples containing each player's name along with their nationality
PASSED
test_grader.py::test_get_players_on_team
Define a function called get_players_on_team that returns a list of the names of all the players who have played on a given team
PASSED

======================= 4 passed in 0.55 seconds =======================
```

## How to use

#### Remotely
[Get a GitHub OAuth Token](https://github.com/settings/tokens) and paste it into the `oauth_token` variable at the top of `remote_grader.py`.

Run:

```
python remote_grader.py -r user/repo-name
```

For example, to test this repo you would run `python remote_grader.py -r learn-co-curriculum/dsc-notebook-test-template`

That's it! The script will use the GitHub API to get the notebook contents, write it to the `index.ipynb` file, and execute the tests.

#### Locally
* Copy the raw json of a student notebook `index.ipynb` file
* Paste into the `index.ipynb` file here
* Run `pytest` from this directory

## Some Notes

#### Where do I Write the Tests?
When `pytest` is run it is [looking for files](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery) that match `test_*.py` or `*_test.py` and will automatically run tests found there. The example tests are written in `test_grader.py` and can be overwritten.

#### Test Writing Guidelines

There are a few examples of tests provided. Some guidelines:

* Function names must start with `test_`. Use a descriptive name as it will be helpful to see in the output
* Tests will display in the order written
* Import variables and functions from notebook module with `index.name_of_thing`
* Within a test_function, the typical pytest syntax is to use `assert`
* Though you can also use unittest matchers
	* (https://docs.python.org/3/library/unittest.html#test-cases) for higher touch testing.  
	* Ex: `assertCountEqual` is used in the examples so that lists are compared regardless of the order of elements
* Use the `explanation_text` function to print italicized explanatory text on a newline

#### Cells that Error
When the notebook is being imported the execution of *every cell is wrapped in a try/except*. This is to ensure that one error in a notebook will not prevent everything else from being tested. The *first line* of any cells that error will be logged to the console when the notebook is being imported during the test run. Ex:

```
* Skipping cell due to error: zebra #this var is not defined
* Skipping cell due to error: players_on_manchester_united = get_players_on_team(players,'Manchester United')
```

#### Matplotlib Limitation
Unfortunately, any cell that has `import matplotlib.pyplot as plt` will error with:

```
NotImplementedError: Implement enable_gui in a subclass
```

since inline graphics are not supported when executing IPython from the console as we are doing here :/
