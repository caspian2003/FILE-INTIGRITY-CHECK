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

4.Enter File Path

After choosing an option,input the path of the file you want to process.

Examples:

Enter the path to the file: C:\Users\SRI HARSHA\Desktop\codex\mr.robot.txt

Enter the path to the file: /home/user/mr.robot.txt

 You can also drag-and-drop the file into the terminal window for quick path entry.

---

5. Sample Outputs:

File integrity tool scan the directory and prints each file's hashes

Option 1 Output:


Displays and stores hash values.

Output file: example.txt.hashes


Option 2 Output:

Compares current and stored hashes.

Alerts if any mismatch is found (highlighting potential tampering).







