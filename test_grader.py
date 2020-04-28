import notebook_importer
import unittest

# STEP 1:
# IMPORT THE NOTEBOOK AS A MODULE
import index

# (Some setup)
def explanation_text(text):
    """italicized + newline+ text + reset to normal"""
    print("\033[3m" + "\n" + text + "\033[0m")

print("\n\n\n\n\n*****************\n| Running Tests |\n*****************\n\n")

# STEP 2:
# WRITE TEST CASES
# Some Notes:
#   * function names must start with `test_`. Use a descriptive name as it will be helpful to see in the output
#   * Tests will display in the order written here
#   * import variables and functions from notebook module with index.<var_name>
#   * Within a test_function, the typical pytest syntax is to use `assert`
#   * Though you can also use unittest matchers
#       (https://docs.python.org/3/library/unittest.html#test-cases)
#       for more nuanced testing.  `assertCountEqual` is used so that lists
#       are compared regardless of the order of elements
#   * Use the `explanation_text` function to print italicized explanatory text on a newline

def test_example():
    explanation_text("An example that will always pass")
    assert True == True

def test_player_names():
    explanation_text("Create a list of all the keys in the players dictionary")
    unittest.TestCase().assertCountEqual(
      index.player_names,
      ['L. Messi', 'Cristiano Ronaldo', 'De Gea', 'Neymar Jr', 'K. De Bruyne']
     )

def test_player_nationalities():
    explanation_text("Create a list of tuples containing each player's name along with their nationality")
    unittest.TestCase().assertCountEqual(
      index.player_nationalities,
      [('L. Messi', 'Argentina'), ('Cristiano Ronaldo', 'Portugal'), ('Neymar Jr', 'Brazil'), ('De Gea', 'Spain'), ('K. De Bruyne', 'Belgium')]
    )

def test_get_players_on_team():
    explanation_text("Define a function called get_players_on_team that returns a list of the names of all the players who have played on a given team")
    unittest.TestCase().assertCountEqual(
      index.get_players_on_team(index.players,'Manchester United'),
      ['Cristiano Ronaldo', 'De Gea']
    )
