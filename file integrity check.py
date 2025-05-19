import hashlib
import json
import pathlib

def compute_hashes(file_path):
    hash_algorithms = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha224': hashlib.sha224(),
        'sha256': hashlib.sha256(),
        'sha384': hashlib.sha384(),
        'sha512': hashlib.sha512()
    }

    chunk_size = 8192
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                for algo in hash_algorithms.values():
                    algo.update(chunk)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
        return None

    return {name: algo.hexdigest() for name, algo in hash_algorithms.items()}


# noinspection PyTypeChecker
def save_hashes(file_path, hashes):
    hash_file = file_path + '.hashes'
    try:
        with open(hash_file, 'w') as f:
            # noinspection PyTypeChecker
            json.dump(hashes, f, indent=4)
        print(f"Hashes saved to {hash_file}")
    except IOError as e:
        print(f"Error saving hashes: {e}")

def load_hashes(hash_file):
    try:
        with open(hash_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Hash file '{hash_file}' not found.")
    except json.JSONDecodeError:
        print(f"Hash file '{hash_file}' is corrupted or invalid.")
    return None

def verify_file(file_path):
    hash_file = file_path + '.hashes'
    saved_hashes = load_hashes(hash_file)
    if not saved_hashes:
        return

    current_hashes = compute_hashes(file_path)
    if not current_hashes:
        return

    print(f"\nVerifying file: {file_path}")
    all_match = True
    for algo in saved_hashes:
        saved = saved_hashes[algo]
        current = current_hashes.get(algo)
        if current == saved:
            print(f"{algo.upper()}: OK")
        else:
            print(f"{algo.upper()}: MISMATCH!")
            all_match = False

    if all_match:
        print("File integrity verified: all hashes match.")
    else:
        print("File integrity check failed: some hashes do not match.")

def main():
    print("File Integrity Check Tool")
    print("1. Compute and save hashes")
    print("2. Verify file integrity")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice not in ('1', '2'):
        print("Invalid choice.")
        return

    raw_path = input("Enter the path to the file: ").strip()

    # Remove surrounding quotes if any
    if (raw_path.startswith('"') and raw_path.endswith('"')) or (raw_path.startswith("'") and raw_path.endswith("'")):
        raw_path = raw_path[1:-1]

    # Normalize path to handle slashes and spaces properly
    file_path = pathlib.Path(raw_path).expanduser().resolve()

    if not file_path.is_file():
        print("The specified path is not a valid file.")
        return

    if choice == '1':
        hashes = compute_hashes(str(file_path))
        if hashes:
            print("\nComputed hashes:")
            for algo, digest in hashes.items():
                print(f"{algo.upper()}: {digest}")
            save_hashes(str(file_path), hashes)
    else:
        verify_file(str(file_path))

if __name__ == "__main__":
    main()