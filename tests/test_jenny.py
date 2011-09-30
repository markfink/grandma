from grandma import jenny_wrapper
from nose.tools import assert_equals


def test_jenny():
    """Test that the interface of the jenny_wrapper works as expected."""
    dims = {
      "os": ["win32", "linux", "solaris"],
      "cmd": ["ls", "rm", "cp", "del", "pwd"],
      "prot": ["telnet", "ssh", "local-machine"],
    }

    incompats = [{
      # windows doesn't support the ls,rm,cp commands
      "os": ["win32"],
      "cmd": ["ls", "rm", "cp"]
    }]

    reqs = [
      # the del command only works on win32
      ["del", "win32"]
    ]
    # print tests that cover all feature pairs, except the incompatible ones
    tests = jenny_wrapper.create_test_cases(dims, 2, incompats=incompats, reqs=reqs)
    assert_equals(len(list(tests)), 16)
