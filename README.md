# AIS3 2020 Developing Security Project

####

- executable2vec
```execute2vec infile outfile```
output file struct:
csv:
function name, vector

vector params: d=200...



## Generate random C source code

```bash
./random-c.py > /tmp/tmp.c
```
## asm2vec environment
run in git main directory
```
git clone https://github.com/lancern/asm2vec.git
export PYTHONPATH="`pwd`/asm2vec:$PYTHONPATH"
source ~/.bashrc
```
## Compile

```bash
gcc /tmp/tmp.c -o /tmp/tmp.out
```

## Convert binary to vector with `asm2vec`

```bash
./execute2vec.sh /tmp/tmp.out ./train_data/vec.csv
```



## Run Classification

[models/scikit-learn Models.ipynb](models/scikit-learn Models.ipynb)

