# FILE-INTEGRITY-CHECK

🔐File Integrity Check:

A robust Python-based CLI utility for verifying file integrity using industry-standard cryptographic hash functions. Designed for cybersecurity practitioners, forensic analysts, and developers to detect unauthorized modifications, corruption, or tampering of files.

--------------------------------------------------

What is File Integrity Checking? 🧬

File integrity checking is a method to ensure that digital files remain unaltered during storage or transmission. This is accomplished by comparing cryptographic hash digests before and after an event (like transfer, update, or access).

Why is it important?

Detects unauthorized modifications (malware injection, unauthorized edits)

Ensures consistency during software deployment or backups

Validates file authenticity in forensic or compliance scenarios

---

How It Works ⚙️

The tool provides two main functions: hashing and verification.

1. Compute and Save Hashes

Reads the file in binary mode and chunked streams (8KB) to handle large files.

Calculates hashes using:

MD5 (128-bit)

SHA-1 (160-bit)

SHA-224

SHA-256 (256-bit)

SHA-384

SHA-512 (512-bit)

Stores all hash values in a JSON file: "filename.hashes."

Note:Here the code compute hashes and hashes will automatically generate and save in hashes file.

2. Verify File Integrity

Loads saved hash values from filename.hashes.
Recomputes current hashes on the same file.

Compares each algorithm's output:

✅ If all hashes match: File integrity is confirmed.

❌ If any hash mismatches: File has been tampered with or corrupted.

--------------------------------------------------

How to Run 🚀

✔️ Requirements:

Python 3.6+
(File integrity check is a python script which is works on only 3.5 and above version).

{ python --version }

{Built-in libraries like Haslib,pathlib,json}

📝 Usage Instructions:

1. Clone or Download the Repository

git clone https://github.com/yourusername/file-integrity-check.git
cd file-integrity-check


2. Run the Program

python "file integrity check.py"

3. Interactive CLI Menu

File Integrity Check Tool
1. Compute and save hashes
2. Verify file integrity
Choose an option (1 or 2):


4. Enter File Path

Use an absolute path or drag-and-drop into terminal.

The script will sanitize and normalize paths before use.


---

Sample Output 📊

Option 1 (Save Hashes):

![Image](https://github.com/user-attachments/assets/d5f646b1-39bd-4bb7-9457-0e8156f1dcd5


Hashes saved to hashes.txt.hashes


Option 2 (Verify Integrity):

Verifying file: example.txt
MD5:     OK
SHA1:    OK
...
File integrity verified: all hashes match.

---

License 📄

Distributed under the MIT License. See LICENSE file for more informtion.




