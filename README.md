# MT79-RSA
## Summary
A school project to develop RSA encryption
## Dependencies
- python 2.7

- Install dependencies :
```
pip install -r requirements.txt
```
## Usages
- Basic usage
```
python rsacli.py -h
```
- Crypt and decrypt a message
```
$ python rsacli.py crypt "test" 2154 5
$ python rsacli.py decrypt ".tz" 2154 5
```
- Crack a message with pub keys
```
$ python rsacli.py decode LHRZNS 211582871 127
```
- Transform string to number or number to string
```
$ python rsacli.py stn toto
$ python rsacli.py nts 405150
```
- Code and decode a number
```
$ python rsacli.py cryptint 54 2154 5
$ python rsacli.py decryptint 658 2154 5
```

## Anatomy
```
├── README.md
├── requirement.txt
├── rsacli.py               <-- cli
├── src                     <-- source director
├── test                    <-- test directory
```
