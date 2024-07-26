# Smart Translator

Smart Translator is a web application that helps you automatically translate text into a target language, with annotations for keywords or specialized terms. This project leverages various language models to provide accurate translations and annotations.

## Features

* **Text Translation** : Translate text into multiple languages.
* **Annotations** : Get annotations for keywords or specialized terms.
* **Streamed Translations** : View translations in real-time as they are processed.

### Key Files and Directories

* **[`Smart_Translator.py`](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "d:\NCKH\Projects\smart-translator\Smart_Translator.py")** : Main entry point for the application.
* **[`components/sidebar/app_sidebar.py`](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "d:\NCKH\Projects\smart-translator\components\sidebar\app_sidebar.py")** : Contains functions to render the sidebar and handle user inputs.
* **[`core/llms.py`](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "d:\NCKH\Projects\smart-translator\core\llms.py")** : Contains logic for language models.
* **[`core/prompts.py`](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "d:\NCKH\Projects\smart-translator\core\prompts.py")** : Contains prompt templates for translations.
* **[`core/translators.py`](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "d:\NCKH\Projects\smart-translator\core\translators.py")** : Contains translation logic.
* **[`utils/consts.py`](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "d:\NCKH\Projects\smart-translator\utils\consts.py")** : Contains application constants.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/smart-translator.git
   cd smart-translator
   ```
2. Create and activate a virtual environment:

   ```
   python -m venv env
   source env/bin/activate
   ```
3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   **streamlit** **run** **Smart_Translator.py**
2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

* [Streamlit](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "https://streamlit.io/") for providing an easy-to-use framework for building web applications.
* All contributors and users for their support and contributions.

## Contact

For any inquiries or issues, please open an issue on the [GitHub repository](vscode-file://vscode-app/c:/Users/phucht2001/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "https://github.com/yourusername/smart-translator/issues").
