<<<<<<< HEAD
Install CMake

Make sure you have CMake installed on your system.
Download and install CMake from here

https://github.com/Kitware/CMake/releases/download/v4.0.1/cmake-4.0.1-windows-x86_64.msi

During installation, ensure that you add CMake to the system PATH.

---------------------------------------------------------------------------------------------------------
Install Visual Studio Build Tools

nmake and other build tools are part of Microsoft Visual Studio Build Tools.
Download and install the Visual Studio Build Tools from here.

https://aka.ms/vs/17/release/vs_BuildTools.exe

During installation, make sure to select the following:
Desktop development with C++
MSVC v142 or v143 - VS 2019 C++ x64/x86 build tools (or the latest available version)
---------------------------------------------------------------------------------------------------------

inside the nl2sql folder, download this file with this link 
https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/resolve/main/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf

---------------------------------------------------------------------------------------------------------

#file path
cd path\to\nl2sql-genai 

---------------------------------------------------------------------------------------------------------

#activate the virtual environment
venv\Scripts\activate.bat 

---------------------------------------------------------------------------------------------------------

#installing dependencies
pip install -r requirements.txt

---------------------------------------------------------------------------------------------------------

#to run the code
streamlit run app.py

---------------------------------------------------------------------------------------------------------

upload the schema file which is in folder data in this nl2sql-genai
---------------------------------------------------------------------------------------------------------
=======
# nl2sql-genai
>>>>>>> 30aba022ce3f31626aad6d226b9aac1a31b47709
