# ShaktiCTF 2025 - Forensics 🕵️ - Binary Reflection

— Made by zelebwr (BNB) ✏️

- [ShaktiCTF 2025 - Forensics 🕵️ - Binary Reflection](#shaktictf-2025---forensics-️---binary-reflection)
  - [🎯 Synopsis](#synopsis)
  - [🔎 Reconnaissance & Initial Analysis](#reconnaissance-and-initial-analysis)
  - [🔓 Vulnerability Exploitation](#vulnerability-exploitation)
    - [Stage 1: Reversing Line Order](#stage-1-reversing-line-order)
    - [Stage 2: Fixing File Signatures](#stage-2-fixing-file-signatures)
  - [📖 Sources](#sources)

## 🎯 Synopsis {#synopsis}

- **Challenge Description**: The truth is hidden in the mirror
- **Provided Artifacts**: corrupt.zip
- **Flag**: shaktictf{pdf_pr3tty_d4m4g3d_f0rm4t}

## 🔎 Reconnaissance & Initial Analysis {#reconnaissance-and-initial-analysis}

From the title and the description itself, we can find out that the hint is something to do with "mirroring" or "reflection". So, the first step we want to do is getting the file and seek out this hint.

```bash
$ wget -O corrupt.zip "https://traboda-arena-shaktictf-2025.s3.amazonaws.com/files/attachments/corrupt_0b82fc85-bdc0-494e-bb28-9d1458d501ef.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA6GUFVMV6HO3NYL6Z%2F20250726%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250726T073533Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=30c62db9286843eedc0bcba1d6c19e98f90acd8174184b383939131d02d66a43"
--2025-07-26 14:36:05--  https://traboda-arena-shaktictf-2025.s3.amazonaws.com/files/attachments/corrupt_0b82fc85-bdc0-494e-bb28-9d1458d501ef.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA6GUFVMV6HO3NYL6Z%2F20250726%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250726T073533Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=30c62db9286843eedc0bcba1d6c19e98f90acd8174184b383939131d02d66a43
Resolving traboda-arena-shaktictf-2025.s3.amazonaws.com (traboda-arena-shaktictf-2025.s3.amazonaws.com)... 3.5.212.225, 16.12.36.95, 52.219.156.199, ...
Connecting to traboda-arena-shaktictf-2025.s3.amazonaws.com (traboda-arena-shaktictf-2025.s3.amazonaws.com)|3.5.212.225|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 20306 (20K) [application/x-zip-compressed]
Saving to: ‘corrupt.zip’

corrupt.zip                        100%[==============================================================>]  19.83K  --.-KB/s    in 0s

2025-07-26 14:36:06 (83.3 MB/s) - ‘corrupt.zip’ saved [20306/20306]
```

Secondly check the file's integrity, [^4]`is it really a .zip file?`

```bash
$ file corrupt.zip
corrupt.zip: Zip archive data, made by v2.0 UNIX, extract using at least v2.0, last modified Jul 25 2025 16:45:28, uncompressed size 21755, method=deflate
```

From that alone we can assume that it's a valid ZIP Archive. We `unzip` it and we get the `corrupt.pdf`. Here, we want to do the same thing again, getting the file's information again.

```bash
$ file corrupt.pdf
corrupt.pdf: data
```

Since we now know the pdf data is corrupted and can't be opened or read, we can now start to look on what the data is contained in the pdf file exactly. We can achieve this by using `hexdump` and `head` or `tail` (for better readability), like so:

```bash
$ hexdump -C corrupt.pdf | head -n 5
00000000  25 3b 45 4f 46 0a 32 31  32 33 36 0a 73 74 61 72  |%;EOF.21236.star|
00000010  74 78 72 65 66 0a 3c 65  33 62 30 34 30 62 35 39  |txref.<e3b040b59|
00000020  34 36 33 31 64 39 63 34  63 36 61 38 30 31 63 38  |4631d9c4c6a801c8|
00000030  30 35 31 38 31 37 37 3e  20 5d 20 3e 3e 0a 3c 3c  |0518177> ] >>.<<|
00000040  20 2f 53 69 7a 65 20 31  38 20 2f 52 6f 6f 74 20  | /Size 18 /Root |

$ hexdump -C corrupt.pdf | tail -n 5
000054c0  20 2f 46 6c 61 74 65 44  65 63 6f 64 65 20 2f 4c  | /FlateDecode /L|
000054d0  65 6e 67 74 68 20 34 35  36 20 3e 3e 0a 33 20 30  |ength 456 >>.3 0|
000054e0  20 6f 62 6a 0a 25 c4 e5  f2 e5 eb a7 f3 a0 d0 c4  | obj.%..........|
000054f0  c6 0a 24 50 44 46 2d 31  2e 33 0a                 |..$PDF-1.3.|
000054fb
```

From here we can already see the vulnerability that we can exploit. If we're familiar with PDF File Structure, we can see there are special characters ([^1]magic numbers or file signatures) that is a necessity for a PDF file: `$PDF-` and `%;EOF`. But we could see that the file signature's characters were a bit [^2][^3]off and in the [^3]wrong positions. The file signature `%;EOF` was supposed to be [^3]`%%EOF` and supposed to be at the end of the file. Meanwhile, the `$PDF-` was supposed to be [^2][^3]`%PDF-`. From that and the hint the title and the description give out, we could assume the content of this file is reversed.

## 🔎 Reconnaissance & Initial Analysis {#reconnaissance-and-initial-analysis}
## 🔓 Vulnerability Exploitation {#vulnerability-exploitation}

The exploitation process will be separated in to two stages.

## 🔎 Reconnaissance & Initial Analysis {#reconnaissance-and-initial-analysis}
### Stage 1: Reversing Line Order {#stage-1-reversing-line-order}

So by the previous reconnaissance, we could deduce that the main problem is the file's lines is in a reverse order. My initial assumption were to use `rev` to reverse the order, but it failed because it revereses the characters within a line, where when attempted the result was a failure.

Thus the solution is solved using `tac` to reverse the lines' order and save it to an output file.

```bash
tac corrupt.pdf > fixed.pdf
```

### Stage 2: Fixing File Signatures {#stage-2-fixing-file-signatures}

After using `tac`, the file was still not recognized as a valid PDF File, because it the file signature is still invalid. We can fix this using the `hexedit` and then change the corresponding incorrect bytes into the correct bytes. So, we change the `24` (`$`) and `3B` (`;`) into the required `25` (`%`). To fix this, I used `hexedit` to manually patch the byte.

```bash
$ hexedit corrupt.pdf
```

From then on, we can just open the PDF file in your PDF File Viewer. We can confirm the success of this through the `file`.

```bash
$ file fixed.pdf
fixed.pdf: PDF document, version 1.3, 1 page(s)
```

In your PDF File Viewer, you'll be able to see the flag on the bottom left corner. The flag: **shaktictf{pdf_pr3tty_d4m4g3d_f0rm4t}**

## 🔎 Reconnaissance & Initial Analysis {#reconnaissance-and-initial-analysis}
## 📖 Sources {#sources}

[^1]: [GCK's File Signatures Table](https://www.garykessler.net/library/file_sigs.html);
[^2]: [List of File Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures); Focus on the ZIP and PDF File Signatures
[^3]: [Adobe PDF 1.7 Specification (File Structure)](https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.7old.pdf); Focus on the "File Structure" section
[^4]: [The structure of a PKZip file](https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html); Focus on the "Local File Headers" section
