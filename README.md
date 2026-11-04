# Lab 6 Code and Branch Coverage Analysis

**Student:** Mayukh  
**SRN:** PES2UG24CS271

This repository contains the Lab 6 calculator application and separate test files for line coverage and branch coverage.

## Run the measurements

```powershell
pip install -r requirements.txt
coverage run --source=calculator -m pytest CodeCoverageTest_calculator.py
coverage report -m
coverage run --branch --source=calculator -m pytest BranchCoverageTest_calculator.py
coverage report -m
```
