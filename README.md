## Installation

- make a virtualenv 
- pip install

Download the relevant network  
```
python -m spacy download en_core_web_trf
```

## Testing

Run tests
```
pytest
```

Update snapshots
```shell
pytest --snapshot-update
```

## Install

Clone repo
```shell
git clone http://onarbooks.com/nikatlas/word_processor.git
pip install ./word_processor
```
Download the relevant network  
```
python -m spacy download en_core_web_trf
```

Run the package's script
```shell
python -m word_processor "A sentence that describes a variable or function or method or class"
```