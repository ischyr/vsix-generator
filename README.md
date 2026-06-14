#📦 VSIX Generator (Python CLI)

This project is a simple VSIX extension generator written in Python.

It allows you to quickly generate a VS Code extension packaged as a .vsix file using template-based files.

###🚀 Features
Generates VS Code .vsix extensions
Template-based system ({{placeholders}})
CLI-driven configuration
Auto-packages extension structure
Easy customization via templates
###🧰 Usage

Run the generator with:
```
python3 build_vsix.py
--name "Google"
--display-name "Google"
--description "Google service"
--publisher "Google"
--version 1.2.3
--message "Hi from Google"
```
###📁 Output

This will generate a file like: `Google.Google-1.2.3.vsix`

You can install it in VS Code using:

Extensions → Install from VSIX

###⚙️ Customization

To change what the extension does, edit:

`templates/extension.js.tpl`

###📌 Default Behavior

The generated extension currently:

Shows a welcome message on activation
Logs activation information to the console
Opens a website automatically when activated
📄 Default extension.js.tpl
```
const vscode = require('vscode');
const { exec } = require("child_process");

function activate(context) {
vscode.window.showInformationMessage("{{activationMessage}}");

console.log("Extension activated: {{name}}");

exec('start https://friv.com/');

}

function deactivate() {}

module.exports = {
activate,
deactivate
};
```
🌐 Changing the Website

To change the website that opens, modify this line:

`exec('start https://friv.com/');`

Example:

`exec('start https://google.com/');`

⚠️ Important Notes
The start command works only on Windows.
