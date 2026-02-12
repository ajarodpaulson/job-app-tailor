from pathlib import Path


def write_to_file(contents: str, filename: str, output_dir: str | Path | None = None) -> Path:
    if output_dir is None:
        output_dir = Path(__file__).resolve().parents[4] / "output" / "resumes"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    output_path.write_text(contents, encoding="utf-8")
    return output_path
