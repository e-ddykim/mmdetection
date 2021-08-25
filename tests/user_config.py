import os
os.environ["TT_SMOKE_TESTS"] = "False"
os.environ["TT_RUN_REGRESSION_TESTS"] = "True"
os.environ["TT_API_OTHER_TESTS"] = "True"
os.environ["TT_PERFORMANCE_TESTS"] = "True"
os.environ["TT_LONG_TESTS"] = "False"
os.environ["TT_MANUAL_TESTS"] = "False"
os.environ["TT_GUI_SMOKE_TESTS"] = "True"
os.environ["TT_GUI_REGRESSION_TESTS"] = "True"
os.environ["TT_GUI_OTHER_TESTS"] = "True"
os.environ["TT_GUI_LONG_TESTS"] = "True"
if "TT_DATABASE_URL" not in os.environ or os.environ["TT_DATABASE_URL"] == "":
    os.environ["TT_DATABASE_URL"] = "mongodb://localhost/impt_develop_test_results"
os.environ["TT_ENVIRONMENT_NAME"] = "lbeynens"