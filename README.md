# acroname-python-cli
CLI for ON/OFF support of Acroname's USBHub3p in python

## Setup
`pip install brainstem-2.3.12-py2-none-any.whl`

## Usage
#### Enabling a port
  `./acroname.py --port 0 --enable`
#### Disabling a port
 `./acroname.py --port 0 --disable`
#### Cycling a port (disables, sleeps 2, then enables)
  `./acroname.py --port 0 --cycle`
