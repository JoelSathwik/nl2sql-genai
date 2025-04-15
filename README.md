Here's the formatted version with the merge conflict markers removed and everything cleaned up:

---

# Install CMake

Make sure you have CMake installed on your system.  
Download and install CMake from here:

[https://github.com/Kitware/CMake/releases/download/v4.0.1/cmake-4.0.1-windows-x86_64.msi](https://github.com/Kitware/CMake/releases/download/v4.0.1/cmake-4.0.1-windows-x86_64.msi)

During installation, ensure that you add CMake to the system PATH.

---

# Install Visual Studio Build Tools

`nmake` and other build tools are part of Microsoft Visual Studio Build Tools.  
Download and install the Visual Studio Build Tools from here:

[https://aka.ms/vs/17/release/vs_BuildTools.exe](https://aka.ms/vs/17/release/vs_BuildTools.exe)

During installation, make sure to select the following:
- Desktop development with C++
- MSVC v142 or v143 - VS 2019 C++ x64/x86 build tools (or the latest available version)

---

Inside the `nl2sql` folder, download this file with the following link:  
[https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/resolve/main/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf](https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/resolve/main/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf)

---

### File Path
```bash
cd path\to\nl2sql-genai
```

---

### Activate the Virtual Environment
```bash
venv\Scripts\activate.bat
```

---

### Installing Dependencies
```bash
pip install -r requirements.txt
```

---

### To Run the Code
```bash
streamlit run app.py
```

---

### Upload the Schema File

Upload the schema file located in the `data` folder inside the `nl2sql-genai` project.

---

Let me know if you need any further adjustments or more help!
