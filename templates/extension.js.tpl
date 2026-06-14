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
}
