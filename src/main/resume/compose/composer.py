import pybars
from pathlib import Path

from write_to_file import write_to_file

_LATEX_ESCAPE_MAP = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}

DEFAULT_NAME = "Jarod Paulson"


def _latex_escape(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    for char, replacement in _LATEX_ESCAPE_MAP.items():
        text = text.replace(char, replacement)
    return text


def compose_resume(name: str | None = None, template_path: str | Path | None = None, output_dir: str | Path | None = None) -> Path:
    if template_path is None:
        template_path = Path(__file__).resolve().parents[1] / "templates" / "jakes_resume.tex"
    else:
        template_path = Path(template_path)

    if not name:
        name = DEFAULT_NAME

    template_source = template_path.read_text(encoding="utf-8")
    compiler = pybars.Compiler()
    template = compiler.compile(template_source)
    rendered = template({"name": _latex_escape(name)})

    filename = f"{name}_resume.tex"
    return write_to_file(rendered, filename, output_dir=output_dir)


def main() -> int:
    output_path = compose_resume()
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
