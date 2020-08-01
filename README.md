# AIS3 2020 Project：自動化行為函式找尋 (*ART - Automated Reverse Tool*)

<!-- MarkdownTOC -->

- [Authors](#authors)
- [動機](#%E5%8B%95%E6%A9%9F)
- [環境與配置](#%E7%92%B0%E5%A2%83%E8%88%87%E9%85%8D%E7%BD%AE)
- [預期成果](#%E9%A0%90%E6%9C%9F%E6%88%90%E6%9E%9C)
- [實作流程](#%E5%AF%A6%E4%BD%9C%E6%B5%81%E7%A8%8B)
- [實作成果](#%E5%AF%A6%E4%BD%9C%E6%88%90%E6%9E%9C)
- [Reference](#reference)

<!-- /MarkdownTOC -->

## Authors
* 組別：軟體安全開發 6th
* 組員
  * 林詠翔 [stdlib.h](https://github.com/r888800009)
  * 林哲宇 [zeze](https://github.com/zeze-zeze)
  * 顏伯勳 [Bronson](https://github.com/bronson113)
  * 謝繼緯 [@tomy0000000](https://github.com/tomy0000000)
* [簡報](https://docs.google.com/presentation/d/1yUHZjCuffwgdU5RMp0XDFAVgkfmwzkDo5ElGYpZmI04)
* [HackMD](https://hackmd.io/tbtjo3e2ScWkXX9sWECrNQ)

## 動機

現已知在調查資安事件時，實際逆向目標檔案通常是最後手段，故希望在必要時能減少逆向所需的時間。當遇到沒見過的 Binary 時，可以自動點出有某行為發生的 Function，以此來增加逆向效率

## 環境與配置

* OS: Ubuntu Linux 20.04 LTS
* Language: C
* Granularity: function level
* 保護機制全開 (CANARY, NX, ASLR, PIE, FULL RELRO)

## 預期成果

* 目的: 找出某種特定行為(此專案以 reverse shell 為例)所在的函式
* 行為: 輸入一個 binary，預期輸出含有特定行為函式的位址

## 實作流程

1. 利用 asm2vec 從 binary 中取出 feature
2. 產生含有 reverse shell 的程式當作 dataset
3. 餵進各種 ML model
4. 重複 1 ~ 3，嘗試不同的 feature、dataset 或 ML model

詳細操作步驟可查詢[Installation Guide](https://github.com/zeze-zeze/2020_AIS3_Project/wiki/Installation-Guide)

## 實作成果

![](https://i.imgur.com/bDoJEMI.png)

## Reference
1. [Accurate and Scalable Cross-Architecture Cross-OS Binary Code Search with Emulation](https://www.researchgate.net/publication/324548857_Accurate_and_Scalable_Cross-Architecture_Cross-OS_Binary_Code_Search_with_Emulation)
2. [Pharos Static Binary Analysis Framework](https://github.com/cmu-sei/pharos)
3. [BitBlaze: A New Approach to Computer Security via Binary Analysis](https://www.researchgate.net/publication/221160696_BitBlaze_A_New_Approach_to_Computer_Security_via_Binary_Analysis)
4. [asm2vec](https://github.com/Lancern/asm2vec)
5. [A similarity metric method of obfuscated malware using function-call graph](https://www.researchgate.net/figure/The-classified-X86-instructions_tbl1_257681429)

