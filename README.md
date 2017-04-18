# acroname-python-cli
CLI for ON/OFF support of Acroname's USBHub3p in python

I put this together in a few minutes to satisfy a requirement I had and nothing more so you can expect that it is a very limited implementation.  

For more information on Acraname's Python API see their refernce guide: https://acroname.com/reference/python/index.html

## Setup
`pip install brainstem-2.3.12-py2-none-any.whl`

## Usage
#### Enabling a port
  `acroname.py --port 0 --enable`
#### Disabling a port
 `acroname.py --port 0 --disable`
#### Cycling a port (disables, sleeps 2, then enables)
  `acroname.py --port 0 --cycle`
