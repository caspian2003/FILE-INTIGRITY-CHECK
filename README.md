# FILE-INTEGRITY-CHECK

# 🔐 File Integrity Check

A robust Python-based CLI utility for verifying file integrity using industry-standard cryptographic hash functions. Designed for cybersecurity practitioners, forensic analysts, and developers to detect unauthorized modifications, corruption, or tampering of files.

## 🧬 What is File Integrity Checking?

File integrity checking ensures that digital files remain unaltered during storage or transmission by comparing cryptographic hash digests before and after an event (e.g., transfer, update, or access).

## 🔍 Why is it Important?
- Detects unauthorized modifications (malware injection, unauthorized edits).
- Ensures consistency during software deployment or backups.
- Validates file authenticity in forensic or compliance scenarios.

## ⚙️ How It Works

The tool provides two main functions: **Hashing** and **Verification**.

### ✅ Compute and Save Hashes
- Reads the file in binary mode and chunked streams (8KB) to handle large files.
- Calculates hashes using:
  - MD5 (128-bit)
  - SHA-1 (160-bit)
  - SHA-224
  - SHA-256 (256-bit)
  - SHA-384
  - SHA-512 (512-bit)
- Stores all hash values in a JSON file: `"filename.hashes"`

> **Note:** The tool automatically generates and saves computed hashes.

### 🔄 Verify File Integrity
- Loads saved hash values from `"filename.hashes"`.
- Recomputes hashes for the file and compares each algorithm’s output:
  - ✅ **If all hashes match:** File integrity is confirmed.
  - ❌ **If any hash mismatches:** File has been tampered with or corrupted.

## 🚀 How to Run

### ✔️ Requirements:
- Python 3.6+  
  _(File Integrity Check works only on Python 3.5 and above)_
- Built-in libraries:
  - `hashlib`
  - `pathlib`
  - `json`

## Usage Instruction:

To check for the python version-
python --version:

```sh
python --version
```

Follow these instruction to use the file integrity tool from cloning to execution:

1.Clone the Repository

```Bash
git clone

https://github.com/caspian2003/file-integrity-check.git

cd file-integrity-check
```

2.Run the script

```
Bash

python "file integrity check.py"
```

3.Choose Options Displayed in terminal

```
File Integrity Check Tool
1.Compute and save hashes
2.Verify file integrity
Choose an Option (1 or 2)
```
#### Option 1: Computes the hash values of a file and saves them to filename.hashes (in JSON format).

#### Option 2: Verifies the current file against its saved hashes to check if the file has been modified.

## 4.Enter File Path

After choosing an option,input the path of the file you want to process.

Examples:

Enter the path to the file: C:\Users\SRI HARSHA\Desktop\codex\mr.robot.txt

Enter the path to the file: /home/user/mr.robot.txt

 You can also drag-and-drop the file into the terminal window for quick path entry.

---

## 5. Sample Outputs:

File integrity tool scan the directory and prints each file's hashes

Option 1 Output:

![Image](https://github.com/user-attachments/assets/564de7e3-abbd-4669-9cfa-ba4c58522fd6)
 
Here you have to select options (1 or 2)

![Image](https://github.com/user-attachments/assets/4ea0b881-3b64-44a9-98fd-187c4b0d1ea3)

```Hash generation
Computed hashes:
MD5:d41d8cd98f00b204e9800998ecf8427e
SHA1: da39a3ee5e6b4b0d3255bfef95601890afd80709
SHA384: 38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b
SHA512: cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a53
8327af927da3e
...
Hashes saved to: C:\Users\SRI HARSHA\Desktop\codex\mr.robot.txt.hashes
This file integrity tool compute and calculate hashes
```

![Image](https://github.com/user-attachments/assets/d7d0dc13-d554-4d11-82d1-9d0070b66c0d)

Integrity verification:
🔒 File unchanged:
```
MD5: OK
SHA1: OK
SHA384: OK
SHA512: OK
...
File integrity verified: all hashes match.
```

![Image](https://github.com/user-attachments/assets/7f09590e-3203-4bde-b222-30146792d30b)

⚠️ File tampered:

```
MD5: MISMATCH!
SHA1: MISMATCH!
SHA384:MISMATCH!
SHA512: MISMATH!
...
File integrity check failed: some hashes do not match.
```

## 📌 Use Cases

Detect tampering in configuration files, scripts, or sensitive documents.

Ensure integrity before deployment or sharing.

Verify forensic evidence file authenticity.

## 🛠️ Technologies Used

Python 3

hashlib module for hash computation

Command-line interface (CLI)

## 📄 License

This project is developed as part of a personal learning initiative and is provided free of charge for educational and non-commercial use only.









