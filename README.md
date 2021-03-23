# Local Python codility environment
Helps quickly setting up local [Codility](https://www.codility.com/) environment for Python

## Why?
Online coding platform Codility gives you the opportunity to solve interesting tasks as well
as pass coding interviews. However, it lacks some important features as syntax checking,
autocompletion and debugging. This repo solves the problem by unifying (as far as this is possible)
your local environment with the IDE of your choice, fast unit tests and all other necessary
features with online.

At the end, this might save you a lot of time during the interview!
## Quick start:
- make sure you have installed the same version of python as used on
Codility platform. (If you have e.g. 3.8 and on Codility it's only 3.6
  it's quite unlikely to make any issues. Still, it's better to have exactly
  the same setup)
- clone this repo
- configure IDE for this project (including proper python interpreter)
- you may also wish to copy-paste and re-name the "sample" folder in advance
- look at example which demonstrates fully working solution from this platform and try to run it.
## During online coding
- copy-paste and re-name the "sample" folder (if not done yet)
- copy content of the task python file into solution.py
- copy content of test-input.txt while removing all comments from there
- optionally copy the test data from examples, and your own 
- for every test data input (line) in test-input.txt make sure you have a respective
line of data in test-expected.txt in a correct format. It's important that both files test-input.txt
  and test-expected.txt are cleaned up from any other symbols and have the same number of lines.
- run tests in test_solution.py when solution() is ready
- when all tests are OK, you may transfer you local code Codility online. This could be easily done
by simply copy-pasting the content of solution(). You might also want to move a testing input data
  from test-input.txt, although it's not necessary. (The content of other file has no peers available
  for the user.)
