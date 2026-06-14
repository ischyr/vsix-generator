#!/usr/bin/env python3

import argparse
import zipfile
import re
from pathlib import Path


# ----------------------------
# Template engine
# ----------------------------

def render_template(text, context):
    """
    Supports:
      {{key}}
      {{nested.key}}
    """

    def lookup(path, data):
        for part in path.split("."):
            if isinstance(data, dict):
                data = data.get(part)
            else:
                return ""
        return "" if data is None else str(data)

    return re.sub(
        r"\{\{([^}]+)\}\}",
        lambda m: lookup(m.group(1).strip(), context),
        text
    )


# ----------------------------
# Load templates
# ----------------------------

def load_templates(template_dir: Path):
    templates = {}

    for file in template_dir.rglob("*.tpl"):
        relative_path = file.relative_to(template_dir)

        # remove .tpl extension
        target_path = str(relative_path).replace(".tpl", "")

        templates[target_path] = file.read_text(encoding="utf-8")

    return templates


# ----------------------------
# Build VSIX
# ----------------------------

def build_vsix(output_file, context, template_dir="templates"):
    templates = load_templates(Path(template_dir))

    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:

        # Required VSIX content types
        zf.writestr("[Content_Types].xml", """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension=".vsixmanifest" ContentType="text/xml" />
  <Default Extension=".json" ContentType="application/json" />
  <Default Extension=".js" ContentType="application/javascript" />
</Types>
""")

        # IMPORTANT FIX:
        # Everything must live under "extension/" folder inside the VSIX
        for path, content in templates.items():

            # ensure correct VS Code structure
            target_path = "extension/" + path

            rendered = render_template(content, context)
            zf.writestr(target_path, rendered)

    print(f"[+] VSIX created: {output_file}")


# ----------------------------
# CLI
# ----------------------------

def main():
    parser = argparse.ArgumentParser(description="VSIX Builder")

    parser.add_argument("--name", required=True)
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--description", default="")
    parser.add_argument("--publisher", required=True)
    parser.add_argument("--version", default="0.0.1")
    parser.add_argument("--message", default="Extension activated")

    args = parser.parse_args()

    context = {
        "name": args.name,
        "displayName": args.display_name,
        "description": args.description,
        "publisher": args.publisher,
        "version": args.version,
        "activationMessage": args.message,
        "engines": {
            "vscode": "^1.60.0"
        }
    }

    output_file = f"{args.publisher}.{args.name}-{args.version}.vsix"

    build_vsix(output_file, context, template_dir="templates")


if __name__ == "__main__":
    main()
