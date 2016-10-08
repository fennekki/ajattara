from setuptools import setup, find_packages

setup(
    name="Ajattara",
    version="0.2.0",
    description="For measuring the runtime of applications",
    url="https://github.com/fennekki/ajattara",
    author="fennekki",
    license="BSD 2-Clause",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points={
        "console_scripts": [
            "ajattara=ajattara.ajattara:run_program"
        ]
    }
)
