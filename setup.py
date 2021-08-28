from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-is-in-given-time-span',
    version='0.1.0',
    description='The purpose of this plugin is to check if the local time is within defined time span.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Marcin Gaca',
    author_email='emygeq@gmail.com',
    packages=['tracardi-local-time-in-given-time-span'],
    install_requires=[
        tracardi_plugin_sdk,
        tracardi-dot-notation,
        pydantic == pydantic 1.8.2,
        pytz == 2021.1,
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)
