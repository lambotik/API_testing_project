# API_testing_project
## To run a project and get an Allure report:
- 1.Open command line (Win+R)
- 2.For check python version at the command line type : ```python --version```
- 3.If python is not installed: https://www.python.org/downloads/
- 4.After installed python
- 5.Copy this line in command line and press enter: 
```git clone https://github.com/lambotik/API_testing_project.git```
- 6.At the command line, type: ```cd API_testing_project```
- 7.At the command line, type: ```pytest --alluredir=test_result/ tests/```
- 8.Wait for all tests to pass, may take up to 4 minutes
- 9.To generate a report: At the command line, type: ```allure serve test_result```
