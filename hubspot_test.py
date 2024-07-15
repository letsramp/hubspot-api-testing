
from tests import (
    contacts_test,
)

global_vars={"properties":["firstname","lastname", "email"], "contactId": "28919092605"}


failure_list = []
def execute_tests(address="localhost:45555", override_code_path="", global_vars=global_vars, endpoint_address="api.hubapi.com", duration=None):
    status_list = []
    status = None
    status=contacts_test.execute_tests(address=address, override_code_path=override_code_path, global_vars=global_vars, endpoint_address=endpoint_address, duration=duration)
    status_list.extend(status)
    print_test_status(test_name="contacts", status=status)
    return status_list

def print_test_status(test_name, status):
    if status.passed():
        print(f"Test case { test_name } passed")
    else:
        print(f"Test case { test_name } failed : { status.failed() }")
        failure_list.append(status.failed())

if __name__ == "__main__":
    status = execute_tests(global_vars=global_vars)
    if len(failure_list) > 0:
        print(f"Some test cases failed : {failure_list}")
        exit(1)
    else:
        print("All test cases passed")
        exit(0)
