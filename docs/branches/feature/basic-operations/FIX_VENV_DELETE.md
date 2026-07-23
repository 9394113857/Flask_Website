# Fix: Unable to Delete Python Virtual Environment (`venv`)

## Problem

While trying to delete the virtual environment, PowerShell shows:

```powershell
Remove-Item : Cannot remove item ...
Access to the path 'python.exe' is denied.
```

This means that `venv\Scripts\python.exe` is currently being used by one or more running Python processes.

---

# Step 1: Check Running Python Processes

Run:

```powershell
Get-Process python, python3 -ErrorAction SilentlyContinue
```

Example output:

```text
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
213      20        46192      54160      1.33      8264    python
72       4         764        3400       0.03      9164    python
```

---

# Step 2: Stop the Running Processes

## Option 1 (Recommended)

Stop specific processes using their Process IDs (PIDs):

```powershell
Stop-Process -Id 8264 -Force
Stop-Process -Id 9164 -Force
```

---

## Option 2

Stop every Python process:

```powershell
Get-Process python | Stop-Process -Force
```

---

## Option 3

Using Command Prompt:

```cmd
taskkill /F /IM python.exe
```

---

# Step 3: Verify Python Is No Longer Running

Run:

```powershell
Get-Process python, python3 -ErrorAction SilentlyContinue
```

If nothing is returned, all Python processes have been stopped.

---

# Step 4: Delete the Virtual Environment

```powershell
Remove-Item -Recurse -Force .\venv
```

If successful, the `venv` folder will be removed.

---

# Step 5: Create a New Virtual Environment

Using Python 3.11:

```powershell
py -3.11 -m venv venv
```

---

# Step 6: Activate the Virtual Environment

PowerShell:

```powershell
.\venv\Scripts\Activate
```

Command Prompt:

```cmd
venv\Scripts\activate
```

---

# Step 7: Upgrade pip

```powershell
python -m pip install --upgrade pip
```

---

# Step 8: Install Project Dependencies

```powershell
python -m pip install -r requirements.txt
```

---

# If "Access Denied" Still Appears

Another application may still be using the virtual environment.

Try the following:

1. Close all VS Code windows.
2. Open **Task Manager** (`Ctrl + Shift + Esc`).
3. End every **python.exe** process.
4. Delete the `venv` folder.
5. Reopen VS Code.
6. Recreate the virtual environment.

---

# Helpful Commands

Check Python version:

```powershell
python --version
```

Locate Python executable:

```powershell
where python
```

Check active virtual environment:

```powershell
echo $env:VIRTUAL_ENV
```

Deactivate current virtual environment:

```powershell
deactivate
```

List installed packages:

```powershell
pip list
```

Freeze dependencies:

```powershell
pip freeze > requirements.txt
```

---

# Troubleshooting Checklist

- ✅ No Python processes are running.
- ✅ VS Code terminals are closed.
- ✅ Virtual environment is deactivated.
- ✅ `venv` folder deleted successfully.
- ✅ New virtual environment created.
- ✅ Virtual environment activated.
- ✅ Dependencies installed.

---

# Expected Workflow

```text
Check running Python processes
        ↓
Stop Python processes
        ↓
Verify no processes remain
        ↓
Delete venv
        ↓
Create new venv
        ↓
Activate venv
        ↓
Upgrade pip
        ↓
Install requirements
        ↓
Run the project
```

---

## Final Commands

```powershell
Get-Process python, python3 -ErrorAction SilentlyContinue

Get-Process python | Stop-Process -Force

Remove-Item -Recurse -Force .\venv

py -3.11 -m venv venv

.\venv\Scripts\Activate

python -m pip install --upgrade pip

python -m pip install -r requirements.txt
```

---

**Status:** ✅ Virtual environment reset procedure complete.
