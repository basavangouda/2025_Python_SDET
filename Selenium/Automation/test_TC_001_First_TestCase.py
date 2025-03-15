import pytest

actual="QACircle"
@pytest.mark.smoke
@pytest.mark.regression
def test_tc_001_login_logout_Testing():
    print("This is out of testcase code")
    print("This is end of testcase code")
    assert actual=="QACircle" #Copmare same

@pytest.mark.sanity
def test_tc_002_login_logout_Testing():
    print("This is out of testcase2 code")
    print("This is end of testcase2 code")
    assert actual == "qacircle" #Compare not same