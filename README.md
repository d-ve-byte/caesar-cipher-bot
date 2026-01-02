# Caesar Cipher Bot

A simple CLI tool to encrypt or decrypt text using the classic Caesar cipher.

## How it works
- Shifts alphabetic characters by a user-provided integer (positive or negative).
- Preserves letter case; non-letters are left unchanged.
- Decryption uses the inverse of the shift.

## Requirements
- Python 3.8+

## Usage
```pwsh
cd "c:\Users\davix\Music\ATLAS\Internship project\caesar cipher bot"
python caesar_cipher.py
```
Then follow the prompts for message, shift, and mode (encrypt/decrypt).

## Notes
- Supports negative shifts.
- Only letters are shifted; numbers/punctuation stay as-is.
