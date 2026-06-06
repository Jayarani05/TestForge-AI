from app.exporters.code_exporter import (
    CodeExporter
)


code = """

from selenium import webdriver


def test_login():

    driver = webdriver.Chrome()

    assert True

"""


exporter = CodeExporter()


result = exporter.export(

    code,

    "python"

)


print(
    result
)