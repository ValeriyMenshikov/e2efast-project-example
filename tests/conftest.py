import os

os.environ["PETSTORE_BASE_URL"] = "https://petstore3.swagger.io/api/v3"

pytest_plugins = ["framework.fixtures.http.petstore_service"]