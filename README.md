# 📦 VSIX Generator (Python CLI)

A simple VSIX extension generator written in Python. Quickly generate a VS Code extension packaged as a `.vsix` file using a template-based system.

---

## 🚀 Features

- Generates VS Code `.vsix` extensions
- Template-based system (`{{placeholders}}`)
- CLI-driven configuration
- Auto-packages extension structure
- Easy customization via templates

---

## 🧰 Usage

Run the generator with:

```bash
python3 build_vsix.py \
  --name "Google" \
  --display-name "Google" \
  --description "Google service" \
  --publisher "Google" \
  --version 1.2.3 \
  --message "Hi from Google"
```

---

## 📁 Output

The command above will generate a file like:

````
Google.Google-1.2.3.vsix
````

Install it in VS Code via:

> **Extensions** → **Install from VSIX...**

---

## ⚙️ Customization

To change what the extension does, edit the template file:

````
templates/extension.js.tpl
````

---

## 📌 Default Behavior

The generated extension:

- Shows a welcome message on activation
- Logs activation information to the console
- Opens a website automatically when activated

---

## 📄 Default `extension.js.tpl`

```js
const vscode = require('vscode');
const { exec } = require("child_process");

function activate(context) {
  vscode.window.showInformationMessage("{{activationMessage}}");
  console.log("Extension activated: {{name}}");
  exec('start https://friv.com/');
}

function deactivate() {}

module.exports = { activate, deactivate };
```

---

## 🌐 Changing the Website

To change the website that opens on activation, modify the following line in your template:

```js
exec('start https://friv.com/');
```

**Example:**

```js
exec('start https://google.com/');
```

---

## ⚠️ Important Notes

> The `start` command is **Windows-only**. For macOS use `open`, and for Linux use `xdg-open`.
