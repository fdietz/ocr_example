# python tesseract

Using [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

Based on the following articles:
- https://nanonets.com/blog/ocr-with-tesseract/
- https://joseurena.medium.com/tesseract-ocr-evaluating-handwritten-text-recognition-1c6db85b2e7f

## requirements

install [tesseract](https://tesseract-ocr.github.io/tessdoc/) library:

```bash
brew install tesseract
```

## install

```bash
pipenv install
```

## run

Activate the pipenv shell:

```bash
pipenv shell
python --version
```

Run the `main.py` file:

```bash
python3 main.py
```

## Multiple languages

list supported languages:

```bash
tesseract --list-langs
```

install more languages:

```bash
# linux
sudo apt-get install tesseract-ocr-[lang]

# MacOS
brew install tesseract-lang
```
