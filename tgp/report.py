import html
from typing import Dict, Any
from .models import Genome
from .genes import GENES

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Token Genome Report - {token_name}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    h1 {{ font-size: 24px; margin-bottom: 4px; }}
    h2 {{ font-size: 18px; margin-top: 24px; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 8px; }}
    th, td {{ border: 1px solid #ddd; padding: 6px 8px; font-size: 13px; }}
    th {{ background-color: #f4f4f4; text-align: left; }}
    .level-NONE {{ color: #555; }}
    .level-LOW {{ color: #2e7d32; }}
    .level-MEDIUM {{ color: #ef6c00; }}
    .level-HIGH {{ color: #c62828; font-weight: bold; }}
    .level-CRITICAL {{ color: #b71c1c; font-weight: bold; }}
  </style>
</head>
<body>
  <h1>Token Genome Report</h1>
  <p><strong>Token:</strong> {token_name}</p>

  <h2>Risk Summary</h2>
  <p class="level-{risk_level}"><strong>Level:</strong> {risk_level} &nbsp;&nbsp; <strong>Score:</strong> {risk_score}</p>

  <h2>Active Genes</h2>
  <table>
    <thead>
      <tr>
        <th>Gene</th>
        <th>Category</th>
        <th>Risk Weight</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
</body>
</html>
"""


def write_html_report(genome: Genome, risk: Dict[str, Any], out_path: str) -> None:
    rows_html = []

    for key, active in genome.genes.items():
        if not active:
            continue
        meta = GENES.get(key)
        desc = meta.description if meta else ""
        category = meta.category if meta else ""
        weight = risk["contributions"].get(key, 0)

        row = f"<tr><td>{html.escape(key)}</td><td>{html.escape(category)}</td><td>{weight}</td><td>{html.escape(desc)}</td></tr>"
        rows_html.append(row)

    html_content = HTML_TEMPLATE.format(
        token_name=html.escape(genome.token_name),
        risk_level=html.escape(risk["level"]),
        risk_score=risk["score"],
        rows="\n      ".join(rows_html) if rows_html else "<tr><td colspan='4'>No active genes detected.</td></tr>",
    )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
