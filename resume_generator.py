import json
from string import Template

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_template():
    with open("resume_template.html", "r", encoding="utf-8") as f:
        return f.read()

def render_list(items, tag="li", cls=""):
    if not items:
        return ""
    return "\n".join([f'<{tag} class="{cls}">{item}</{tag}>' for item in items])

def render_resume(data, template):
    from jinja2 import Template as JinjaTemplate

    jinja_template = JinjaTemplate(template)
    return jinja_template.render(**data)

def main():
    data = load_data()
    template = load_template()
    rendered = render_resume(data, template)

    with open("resume.html", "w", encoding="utf-8") as f:
        f.write(rendered)
    print("✅ resume.html generated successfully.")

if __name__=="__main__":
    main()