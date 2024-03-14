from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Game of Life",
    version="1.0.0",
    author="Amir Abu Hani",
    author_email="amirabuhani.cs@gmail.com",
    description="Game of Life project is implement the Conway's Game of Life by simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmirAbuhani/game_of_life",
    packages=find_packages(),
    install_requires=[],  # Add your project dependencies here
    entry_points={
        "console_scripts": [
            "game_of_life = game_of_life.simulator_in_cli:main"
        ]
    },
)





