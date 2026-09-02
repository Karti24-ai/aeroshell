# AeroShell 🚀

A lightweight, non-sandboxed custom terminal emulator shell engine built natively using Python 3.12. Designed to mimic the minimalist aesthetic of the macOS and UNIX shell environments directly inside a Windows host container.

## Key Features ✨
- **UNIX-Style Prompt Interface:** Streamlined workspace prompt displaying `user@hostname workspace %` with custom high-contrast Cyan directory path indicators.
- **Dynamic Package Distribution (`kget`):** An integrated universal software installation framework that resolves local shortcuts or dynamically queries global cloud repositories to install desktop applications seamlessly.
- **System Telemetry Macros:** Native execution macros including custom hardware configurations and environment context monitors.
- **Non-Sandboxed Runtime Execution:** Direct binding subsystem that safely pipes standard binary console inputs to the OS kernel without thread latency or execution limits.

## Production Installation 🛠️
```powershell
# Clone the repository asset files
git clone https://github.com
cd aeroshell

# Compile natively into a standalone desktop application executable (.exe)
python -m PyInstaller --onefile --console aeroshell.py
```
