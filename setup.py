import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-Implementation"
AUTHOR_USER_NAME = "Aayush Thakkar"
SRC_REPO = "end_to_end_ml_project"
AUTHOR_EMAIL = "aayusht2004@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/aayush29114/end_to_end_ml_project",
    project_urls={
        "Bug Tracker": f"https://github.com/aayush2914/end_to_end_ml_project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)