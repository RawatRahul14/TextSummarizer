import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "rawatrahul14"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rahulrawat272chd@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "An advanced text summarization library that extracts key information from lengthy texts using state-of-the-art NLP techniques.",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)