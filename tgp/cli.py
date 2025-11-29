import argparse
import json
import os

from .loader import load_sources, ensure_genomes
from .extractor import extract_genes
from .genes import GENES
from .risk import compute_risk
from .report import write_html_report


def run_scan(path: str, show_inactive: bool) -> None:
    sources = load_sources(path)
    if not sources:
        print("No Solidity files found at the given path.")
        return

    out_dir = ensure_genomes()
    print(f"Extracting genomes from {len(sources)} file(s)...\n")

    for name, src in sources.items():
        genome = extract_genes(name, src)
        risk = compute_risk(genome)

        safe_name = name.replace("/", "_").replace("\\", "_")
        json_path = os.path.join(out_dir, safe_name + ".json")
        html_path = os.path.join(out_dir, safe_name + ".html")

        # write JSON genome
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "token": name,
                    "genes": genome.genes,
                    "risk": risk,
                },
                f,
                indent=2,
            )

        # write HTML report
        write_html_report(genome, risk, html_path)

        # print summary
        print(f"=== {name} ===")
        print(f"Risk: {risk['level']} (score={risk['score']})")

        for key, active in genome.genes.items():
            if not active and not show_inactive:
                continue
            meta = GENES.get(key)
            desc = meta.description if meta else ""
            status = "ACTIVE" if active else "inactive"
            print(f" {key:25} {status:7} {desc}")

        print(f"JSON:  {json_path}")
        print(f"HTML:  {html_path}\n")


def _active_genes_from_single_path(path: str):
    sources = load_sources(path)
    if not sources:
        raise SystemExit(f"No Solidity file found at: {path}")
    # if directory, just take the first file
    name, src = next(iter(sources.items()))
    genome = extract_genes(name, src)
    active = {k for k, v in genome.genes.items() if v}
    return name, active


def run_compare(path_a: str, path_b: str) -> None:
    name_a, genes_a = _active_genes_from_single_path(path_a)
    name_b, genes_b = _active_genes_from_single_path(path_b)

    shared = sorted(genes_a & genes_b)
    only_a = sorted(genes_a - genes_b)
    only_b = sorted(genes_b - genes_a)

    print(f"Comparing:")
    print(f"  A: {name_a}")
    print(f"  B: {name_b}\n")

    print("Shared active genes:")
    if shared:
        for g in shared:
            print(f"  - {g}")
    else:
        print("  (none)")

    print("\nActive only in A:")
    if only_a:
        for g in only_a:
            print(f"  - {g}")
    else:
        print("  (none)")

    print("\nActive only in B:")
    if only_b:
        for g in only_b:
            print(f"  - {g}")
    else:
        print("  (none)")


def main():
    parser = argparse.ArgumentParser(
        prog="tgp-scan",
        description="Token Genome Project – scan or compare token genomes.",
    )
    parser.add_argument(
        "path",
        help="Primary path: .sol file or directory.",
    )
    parser.add_argument(
        "--mode",
        choices=["scan", "compare"],
        default="scan",
        help="Mode of operation: 'scan' (default) or 'compare'.",
    )
    parser.add_argument(
        "--other",
        help="Second .sol file or directory when using --mode compare.",
    )
    parser.add_argument(
        "--show-inactive",
        action="store_true",
        help="Also show inactive genes in scan mode.",
    )

    args = parser.parse_args()

    if args.mode == "scan":
        run_scan(args.path, args.show_inactive)
    elif args.mode == "compare":
        if not args.other:
            raise SystemExit("In compare mode you must provide --other <path_b>.")
        run_compare(args.path, args.other)
