# Python Super Downloader

## Setting up
#### Clone the source code

#### Generate lock file
Use the package manager [pipenv](https://pypi.org/project/pipenv/) to use.
```bash
pipenv lock
```

#### Install all packages
```bash
pipenv install
```

#### Run setup file to install all local packages
```bash
pipenv run runSetup
```

#### Run the program to download sample url
```bash
pipenv runExample
```
After commanding the downloaded pdf file locates in /downloaded folder

## How to run program
#### Option 1: Run from pipenv
```bash
pipenv run python src/main.py download <some-downloadable-url>
```
####Option 2: Using pipenv shell
Go to pipenv virtual environment
```bash
pipenv shell
```

Run the program using command line
```bash
python src/main.py download <some-downloadable-uirl>
```
