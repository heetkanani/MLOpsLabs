# Github LAB2 - MLOps (IE-7374) 

This lab focuses on 5 modules, which includes creating a virtual environment, creating a GitHub repository, creating Python files, creating test files using pytest and unittest, and implementing GitHub Actions.



## Step 1: Creating a Virtual Environment

In software development, it's crucial to manage project dependencies and isolate your project's environment from the global Python environment. This isolation ensures that your project remains consistent, stable, and free from conflicts with other Python packages or projects. To achieve this, we create a virtual environment dedicated to our project. <br>
<br>
To create a virtual environment, follow these steps:

1. Open a Command Prompt or Terminal in the directory where you want to create your project.
2. Choose a name for your virtual environment (e.g "github_lab_02") and run the appropriate command:
    ```
    python -m venv github_lab_02
    ```
3. Activate the virtual environment
    ```
    github_lab_02\Scripts\activate
    ```
After activation, you will see the virtual environment's name in your command prompt or terminal, indicating that you are working within the virtual environment.


## Step 2: Creating a GitHub Repository, Cloning and Folder Structure
Now that we have set up our virtual environment, the next step is to create a GitHub repository for our project and establish a structured folder layout. This organization helps maintain your project's code, data, and tests in an organized manner.



### Cloning the Repository
- Open a Command Prompt or Terminal.
- Navigate to the directory where you want to clone your GitHub repository. This should be the same directory where you created your virtual environment.
- Run the following command to clone your GitHub repository into the current directory:
    ```
    git clone https://github.com/heetkanani/MLOpsLabs.git
    ```

### Establishing Folder Structure

Once you have cloned your repository, you can establish a structured folder layout within it. This layout helps organize your project into key directories for code, data, and tests. Create the following folder structure within your repository:
```
Github_Labs/
└── Lab1/
    ├── src/
    │   ├── __init__.py
    │   └── calculator.py
    ├── test/
    │   ├── __init__.py
    │   ├── test_pytest.py
    │   └── test_unittest.py
    ├── workflows/
    │   ├── github_lab1_pytest_action.yml
    │   └── github_lab2_unittest_action.yml
    ├── README.md
    └── requirements.txt
```

**Folder Descriptions:**
- **src/**: This folder is where you'll store your project's source code files (calculator.py).
- **test/**: This folder is dedicated to unit tests and test scripts for your code.
- **workflows/**: This folder contains GitHub Actions workflow files for CI/CD automation.
- **__init__.py**: These empty files make Python treat the directories as packages.
- **requirements.txt**: Lists all Python dependencies for the project.
- **README.md**: Project documentation and setup instructions.

### Adding and Pushing Your Project Code to GitHub
Now that we have our virtual environment set up, the GitHub repository created, and the folder structure organized, let's add our project's code and push it to GitHub. 

**Adding Your Project Code** <br>
- Navigate to your project directory using the Command Prompt or Terminal, where you have the virtual environment and folder structure set up.
- Create and write your Python code or other project files within the specified directories (src, data, etc.) according to your project requirements.
- Once your project files are ready, it's time to add them to Git's staging area. In your project directory, run the following command:
    ```
    git add .
    ```
- This command stages all the changes and new files in your project directory for the next commit.

**Committing Your Changes** <br>
- After staging your changes, commit them with a meaningful commit message that describes the changes you made. Replace <your_commit_message> with a descriptive message:
    ```
    git commit -m "<your_commit_message>"
    ```

**Pushing to GitHub** <br>
- To push your committed changes to your GitHub repository, use the following command:
    ```
    git push origin main
    ```
## Step 3: Creating calculator.py in src Folder
- In this step, we create a Python script named calculator.py within the src folder of your project. This script contains a set of mathematical functions designed to perform basic and advanced arithmetic operations.

### Basic Functions:
* fun1(x, y) adds two input numbers, x and y.
* fun2(x, y) subtracts y from x.
* fun3(x, y) multiplies x and y.
* fun4(x, y, z) adds three numbers together and returns their sum.

### Additional Functions (New):
In addition to the basic operations, five more functions have been implemented:
- **func5(x, y)** - Division: Divides x by y with error handling for division by zero.
- **func6(x, y)** - Power: Raises x to the power of y.
- **func7(*args)** - Average: Calculates the average of multiple numbers using variable arguments.
- **func8(x, y)** - Modulo: Returns the remainder when x is divided by y, with error handling for modulo by zero.
- **func9(x)** - Square Root: Calculates the square root of x with validation for negative numbers.

- To view the code and gain a deeper understanding, please refer to the calculator.py file located under the src folder in this [link](https://github.com/raminmohammadi/MLOps/blob/main/src/lab1/calculator.py).

> **Note:** <br>
Whenever you want to push files to your repository follow this step
[Adding and Pushing Your Project Code to GitHub](#adding-and-pushing-your-project-code-to-github)

## Step 4: Creating tests using Pytest and Unittests
- In this step, we'll set up unit tests for the functions in our calculator.py script using two popular testing frameworks: [pytest](https://docs.pytest.org/en/7.4.x/) and [unittest](https://docs.python.org/3/library/unittest.html). Unit testing ensures that individual components of your code work as expected, helping you catch and fix bugs early in the development process.

**Using Pytest** <br>
- Installation (if not already installed):
- If you haven't already installed pytest, you can do so using pip:
    ```
    pip install pytest
    ```
### Writing Pytest Tests
- Pytest makes it easy to write tests for your Python code. Tests are written as regular Python functions, and test file names typically start with test_ or end with _test.py.
- To run your Pytest tests, you can use the pytest command followed by the name of the test file or directory containing your tests:
    ```
    pytest test_sample.py
    ```
- Pytest automatically discovers test functions based on naming conventions. It searches for functions starting with test_ or ending with _test, and it can discover tests in subdirectories as well. This makes it easy to organize your tests.
- Pytest supports parametrized tests, which allow you to run the same test function with multiple sets of inputs and expected outputs. This is particularly useful for testing functions with different input scenarios. Please refer the commented out code in the test_pytest.py file for your reference.
- Let's create a test file named test_pytest.py within the test folder. This file will contain a series of test functions, each aimed at verifying the behavior of specific functions within calculator.py.
- We've prepared test functions (test_fun1, test_fun2, test_fun3, test_fun4, test_func5, test_func6, test_func7, test_func8, and test_func9) to test all nine functions within calculator.py. Each test function uses the assert statement to validate the expected outcomes. Refer the file under test folder for your [reference](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/test/test_pytest.py).
- By running these pytest tests, you can verify that your calculator functions are working correctly.

### Writing Tests with UnitTest
- Unittest allows you to write tests as classes that inherit from the unittest.TestCase class. Test methods are identified by their names, which must start with "test_" to be recognized as test cases.
- To run Unittest tests, you typically execute your test script, which should include a call to unittest.main() at the end. Here's how you can run the tests:
    ```
    python test_sample.py
    ```
- Unittest relies on test discovery, which means it will find test methods based on naming conventions, similar to Pytest. Test methods must start with "test_" to be recognized as test cases.
- Unittest provides a variety of assertion methods, such as assertEqual, assertTrue, assertFalse, and others, to check conditions in your tests. You can choose the assertion method that best suits your testing needs.
- Let's create a test file named test_unittest.py within the test folder. This file will contain a series of test functions, each aimed at verifying the behavior of specific functions within calculator.py.
- We've prepared test methods (test_fun1, test_fun2, test_fun3, test_fun4, test_func5, test_func6, test_func7, test_func8, and test_func9) to test all nine functions within calculator.py. Each test function uses the self.assertEqual statement to validate the expected outcomes. Refer the file under test folder for your [reference](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/test/test_unittest.py).
- By running these unittest tests, you can verify that your calculator functions are working correctly.

## Step 5. Implementing GitHub Actions
- GitHub Actions is a powerful automation and CI/CD (Continuous Integration/Continuous Deployment) platform provided by GitHub. It enables you to automate various workflows and tasks directly within your GitHub repository. GitHub Actions can be used for a wide range of purposes, such as running tests, deploying applications, and automating release processes.

**How GitHub Actions Work:** <br>

- GitHub Actions work based on events, actions, and triggers:
- **Events:** These are specific activities that occur within your GitHub repository, such as code pushes, pull requests, or issue comments. GitHub Actions can respond to these events.
- **Actions:** Actions are individual tasks or steps that you define in a workflow file. These tasks can be anything from building your code to running tests or deploying your application.
- **Triggers:** Triggers are conditions that cause a workflow to run. They can be based on events (e.g., a new pull request) or scheduled to run at specific times.

**The Purpose of GitHub Actions:** <br>

- GitHub Actions serves several purposes:
- **Automation:** It automates repetitive tasks, reducing manual effort and ensuring consistency in your development process.
- **Continuous Integration (CI):** It allows you to set up CI pipelines to automatically build, test, and validate your code changes whenever new code is pushed to the repository.
- **Continuous Deployment (CD):** It enables automatic deployment of your application when changes are merged into a specific branch, ensuring a smooth and reliable release process.

### Using Pytest and Unittest with GitHub Actions:
- Integrating Pytest and Unittest with GitHub Actions can significantly improve the quality and reliability of your codebase. Here's how:
- Pytest with GitHub Actions: You can create a GitHub Actions workflow (e.g., pytest_action.yml) that specifies the steps for running your Pytest tests. When events like code pushes or pull requests occur, GitHub Actions will automatically trigger the workflow, running your Pytest tests and reporting the results back to you. This helps you catch bugs and ensure that your code meets quality standards early in the development process.
- Unittest with GitHub Actions: Similarly, you can create a separate GitHub Actions workflow (e.g., unittest_action.yml) to run your Unittest tests. This ensures that both your Pytest and Unittest suites are executed automatically whenever code changes are made or pull requests are submitted. It provides a robust validation mechanism for your codebase.
- When collaborating in teams, the automated testing process ensures that all test cases pass successfully before allowing the merge of a pull request into the main branch.

### Creating GitHub Actions Workflow Files:
- To implement Pytest and Unittest with GitHub Actions, you'll create two workflow files under the .github/workflows directory in your repository: pytest_action.yml and unittest_action.yml. These workflow files define the specific actions and triggers for running your tests.

**pytest_action.yml** <br>
Please refer [this](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/workflows/pytest_action.yml) file for your reference

1. **Workflow Name:** The workflow is named "Testing with Pytest" with run-name "Pytest Testing."

2. **Event Trigger:** The workflow triggers on:
   - Push events to the main branch
   - Pull request events targeting the main branch

3. **Environment Variables:**
   - PYTHONPATH is set to ./src to ensure proper module imports

4. **Jobs:** The workflow contains a single job named "test," which runs on the ubuntu-latest virtual machine environment.

5. **Steps:**
   - **Checkout code:** This step checks out the code from the repository using actions/checkout@v4.
   - **Set up Python:** It sets up the Python environment using actions/setup-python@v5 and specifies Python version 3.8, with pip caching enabled.
   - **Install dependencies:** This step upgrades pip and installs project dependencies from requirements.txt, along with pytest, pytest-cov, pytest-html, and flake8 for testing and linting.
   - **Lint code:** Runs flake8 on src/ and tests/ directories with a max line length of 88 characters. This step continues even if linting issues are found.
   - **Run tests with coverage:** The core testing step runs Pytest with multiple options:
     - `--cov=src`: Generates coverage report for the src directory
     - `--cov-report=xml` and `--cov-report=term`: Outputs coverage in XML and terminal formats
     - `--junitxml=pytest-report.xml`: Generates JUnit XML report
     - `--html=pytest-report.html --self-contained-html`: Creates a self-contained HTML report
     - `-v`: Verbose output
   - **Check coverage threshold:** Verifies that code coverage is at least 75%, continuing even if threshold is not met.
   - **Upload test results:** In this step, the generated reports (XML, HTML, and coverage files) are uploaded as artifacts using actions/upload-artifact@v4. This runs regardless of test success or failure.
   - **Test Summary:** If tests pass, displays a success message and confirms that coverage report and test results were uploaded.
   - **Test Failure:** If tests fail, displays a failure message indicating that coverage or linting issues may have occurred.

**unittest_action.yml** <br>
Please refer [this](https://github.com/raminmohammadi/MLOps/blob/main/Github_Labs/Lab1/workflows/unittest_action.yml) file for your reference

1. **Workflow Name:** This GitHub Actions workflow is named "Python Unittests."

2. **Event Trigger:** The workflow is triggered by:
   - Push events to the main branch
   - Pull request events targeting the main branch

3. **Jobs:** The workflow defines a single job named "build" that runs on the ubuntu-latest virtual machine environment.

4. **Steps:**
   - **Checkout code:** This step uses the actions/checkout@v4 action to check out the code from the repository. It ensures that the workflow has access to the latest code.
   - **Set up Python:** The "Set up Python" step uses the actions/setup-python@v4 action to configure the Python environment. It specifies that Python version 3.8 should be used.
   - **Display Python version:** Runs `python --version` to display the Python version being used in the workflow.
   - **Upgrade pip:** Explicitly upgrades pip to the latest version using `pip install --upgrade pip`.
   - **Install dependencies:** This step runs the command `pip install -r requirements.txt` to install the project's Python dependencies. It assumes that the project's dependencies are listed in the requirements.txt file.
   - **List installed packages:** Runs `pip list` to display all installed Python packages for debugging and verification purposes.
   - **Run unittests:** In this step, the unittest tests are executed using the command `python -m unittest test.test_unittest -v`. It runs the unittest test suite defined in the test.test_unittest module with verbose output.
   - **Notify on success:** This step uses conditional logic with `if: success()` to check if all the unittest tests passed successfully. If they did, it runs the message "Unit tests passed successfully."
   - **Notify on failure:** Similarly, this step uses conditional logic with `if: failure()` to check if any of the unittest tests failed. If any test failed, it runs the message "Unit tests failed."


## Steps to Run the Lab

### 1. Clone and Setup
```bash
git clone https://github.com/heetkanani/MLOpsLabs.git
cd Lab1
python -m venv github_lab_02
github_lab_02\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Tests
```bash
pytest test/test_pytest.py -v

python -m unittest test.test_unittest -v
```

### 3. Setup GitHub Actions
```bash
mkdir -p .github/workflows
cp workflows/github_lab1_pytest_action.yml .github/workflows/
cp workflows/github_lab2_unittest_action.yml .github/workflows/
git add .
git commit -m "Add calculator with tests and CI/CD"
git push origin main
```

### 4. Verify
- Go to GitHub → **Actions** tab
- Check both workflows show green checkmarks

**Expected Output:** All 9 tests pass (fun1-fun4, func5-func9)

---

**Quick Commands:**
```bash
pytest test/test_pytest.py -v && python -m unittest test.test_unittest -v
```