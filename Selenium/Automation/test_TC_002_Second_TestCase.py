import pytest

@pytest.fixture(scope="module")
def fixture_code():
    print("Executing before test execution")
    print("------------------")
    yield
    print("Executing after test execution")


@pytest.mark.smoke
def test_tc_0021_login_logout_Testing(fixture_code):
    print("This is out of testcase code")
    print("This is end of testcase code")


@pytest.mark.regression
def test_tc_0022_login_logout_Testing(fixture_code):
    print("This is out of testcase2 code")
    print("This is end of testcase2 code")
