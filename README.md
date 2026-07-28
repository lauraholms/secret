
# Secure Notes Manager

Secure Notes Manager is a Python application for securely storing personal notes using AES-256 encryption.

All notes remain encrypted on disk and are only decrypted after successful authentication.

## Features

- AES-256 encryption
- Master password
- Local encrypted storage
- Note search
- JSON export
- Backup support

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

## Example

```
1. Add note
2. View notes
3. Search
4. Export
5. Exit
```

## Future Improvements

- Tags
- Rich text
- Dark mode
- SQLite backend
- Cloud sync (optional)
