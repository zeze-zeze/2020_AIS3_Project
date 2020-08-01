<<<<<<< HEAD
# github README 2020 AIS3 Project
## Team Info
* 組別: 軟體安全開發 6th
* 組員: 林詠翔 stdlib.h, 林哲宇 zeze, 顏伯勳 Bronson, 謝繼緯 Tomy
* [簡報](https://docs.google.com/presentation/d/1yUHZjCuffwgdU5RMp0XDFAVgkfmwzkDo5ElGYpZmI04/edit#slide=id.g8edbfa2c57_2_1)

## 專案說明
### 主題
自動化行為函式找尋 ART - Automated Reverse Tool

### 動機
現已知在調查資安事件時，實際逆向目標檔案通常是最後手段，故希望在必要時能減少逆向所需的時間。當遇到沒見過的 Binary 時，可以自動點出有某行為發生的 Function，以此來增加逆向效率

### 環境與配置
* OS: linux
* Language: C
* Granularity: function level
* 保護機制全開(CANARY, NX, ASLR, PIE, FULL RELRO)

### 預期成果
* 目的: 找出某種特定行為(此專案以 reverse shell 為例)所在的函式
* 行為: 輸入一個 binary，預期輸出含有特定行為函式的位址

### 實作流程
1. 利用 asm2vec 從 binary 中取出 feature
2. 產生含有 reverse shell 的程式當作 dataset
3. 餵進各種 ML model
4. 重複 1~3，嘗試不同的 feature、dataset 或 ML model 

### 實作成果
![](https://i.imgur.com/bDoJEMI.png)

### Reference
1. [Accurate and Scalable Cross-Architecture Cross-OS Binary Code Search with Emulation](https://www.researchgate.net/publication/324548857_Accurate_and_Scalable_Cross-Architecture_Cross-OS_Binary_Code_Search_with_Emulation)
2. [Pharos Static Binary Analysis Framework](https://github.com/cmu-sei/pharos)
3. [BitBlaze: A New Approach to Computer Security via Binary Analysis](https://www.researchgate.net/publication/221160696_BitBlaze_A_New_Approach_to_Computer_Security_via_Binary_Analysis)
4. [asm2vec](https://github.com/Lancern/asm2vec)
5. [A similarity metric method of obfuscated malware using function-call graph](https://www.researchgate.net/figure/The-classified-X86-instructions_tbl1_257681429)
=======
# AIS3 2020 Developing Security Project

####

- executable2vec
```execute2vec infile outfile```
output file struct:
csv:
function name, vector

vector params: d=200...



## Generate Vectors

```bash
python main.py
```





## Generate random C source code

```bash
./random-c.py > ./tmp/tmp.c
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
gcc ./tmp/tmp.c -o ./tmp/tmp.out
```

## Convert binary to vector with `asm2vec`

```bash
./execute2vec.sh ./tmp/tmp.out ./train_data/vec.csv
```



## Run Classification

[models/scikit-learn Models.ipynb](models/scikit-learn Models.ipynb)

>>>>>>> a4b060b351f0a044120f21412e332929770f6d2b
