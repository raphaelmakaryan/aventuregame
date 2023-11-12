import json


def md_creation():
    with open("../save/choix.json") as history:
        history_json = json.load(history)

    markdown_content = ""

    for chapter in history_json["history"]:
        markdown_content += f"# {chapter['Chapter_name']} \n"
        markdown_content += f"### {chapter['Text']} \n"
        markdown_content += f"### {chapter['Choice']} \n\n"

    with open("../save/history.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)
md_creation()