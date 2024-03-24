# README
New project generated from my cookiecutter template.

## Features
1. Logging via Loguru
2. .env loading via python-dotenv
3. Dockerfile to run the script in a container

## Usage
### Running locally
First run to setup virtualenv and run locally with debugging.
```bash
mkvenv
./main.py --debug
```

### Run with Dockerfile
Build image and run
```bash
docker build -t new-project .
docker run new-project --debug
```
