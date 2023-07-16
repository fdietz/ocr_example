# python tesseract

Using [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

Install pipenv:

```bash
pip install pipenv --user
```

Based on the following articles:
- https://nanonets.com/blog/ocr-with-tesseract/
- https://joseurena.medium.com/tesseract-ocr-evaluating-handwritten-text-recognition-1c6db85b2e7f
- https://github.com/JPLeoRX/opencv-text-deskew/tree/master/python-service/services

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

You might have to export the `TESSDATA_PREFIX` environment variable.

```bash
export TESSDATA_PREFIX=/opt/homebrew/Cellar/tesseract-lang/4.1.0/share/tessdata
```
