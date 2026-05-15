#!/usr/bin/env python3
"""lodestone-score: measure a work product against Lodestone concepts via Touchstone.

Reads a work file and a source file, runs Touchstone's measure(), and formats
the result as a Lodestone report covering four operationalized concepts:

  - Verified / Not verified (Section II Verify step)
      -> Touchstone Layer 11 grounding decomposition (G/F/P)
  - Quality theater (Section V failure shape)
      -> Touchstone Layer 10 substance-vs-presentation gap
  - Assumption over verification (Section V failure shape)
      -> Touchstone Layer 4 source matching (unsourced rate)
  - Default implementation (Section VI specificity tests)
      -> Touchstone Layer 1a baseline document generation (not run by default)

Requires clarethium_touchstone. See https://github.com/Clarethium/touchstone.

Concept mapping: see tools/lodestone-via-touchstone.md.

Exit codes:
  0 - All measurable concepts within thresholds.
  1 - At least one concern threshold tripped.
  2 - Error (file not found, encoding error, Touchstone import failed,
      Touchstone measure() raised).

Usage:
  lodestone-score --work path/to/work.txt --source path/to/source.txt

Threshold knobs (defaults are heuristic; tune to context):
  --projected-threshold (default 0.30)
  --gap-threshold (default 0.0)
  --unsourced-threshold (default 0.30)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Score a work product against Lodestone concepts via Touchstone.",
        epilog="See tools/lodestone-via-touchstone.md for the concept mapping.",
    )
    parser.add_argument(
        "--work",
        required=True,
        type=Path,
        help="Path to the work file (the AI output or work product to score).",
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to the source file (what the work was derived from or against).",
    )
    parser.add_argument(
        "--projected-threshold",
        type=float,
        default=0.30,
        help="Projected proportion threshold for Verified/Not verified concern (default: 0.30).",
    )
    parser.add_argument(
        "--gap-threshold",
        type=float,
        default=0.0,
        help="Quality profile gap threshold for Quality theater concern (default: 0.0).",
    )
    parser.add_argument(
        "--unsourced-threshold",
        type=float,
        default=0.30,
        help="Unsourced rate threshold for Assumption over verification concern (default: 0.30).",
    )
    args = parser.parse_args()

    # Read input files.
    try:
        work_text = args.work.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: work file not found: {args.work}", file=sys.stderr)
        return 2
    except UnicodeDecodeError as e:
        print(f"Error: work file is not UTF-8: {e}", file=sys.stderr)
        return 2

    try:
        source_text = args.source.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: source file not found: {args.source}", file=sys.stderr)
        return 2
    except UnicodeDecodeError as e:
        print(f"Error: source file is not UTF-8: {e}", file=sys.stderr)
        return 2

    # Import Touchstone defensively.
    try:
        from clarethium_touchstone import measure
    except ImportError:
        print(
            "Error: clarethium_touchstone is not installed.\n"
            "\n"
            "Install from https://github.com/Clarethium/touchstone:\n"
            "\n"
            "  git clone https://github.com/Clarethium/touchstone.git\n"
            "  cd touchstone\n"
            "  python3 -m venv .venv\n"
            "  source .venv/bin/activate\n"
            "  pip install -e .\n",
            file=sys.stderr,
        )
        return 2

    # Run measurement.
    try:
        result = measure(work_text, source=source_text)
    except Exception as e:
        print(f"Error: Touchstone measure() raised {type(e).__name__}: {e}", file=sys.stderr)
        return 2

    # Extract signals defensively.
    gd = result.get("grounding_decomposition", {}) or {}
    gfp = gd.get("proportions", {}) or {}
    grounded = float(gfp.get("G", 0.0) or 0.0)
    framed = float(gfp.get("F", 0.0) or 0.0)
    projected = float(gfp.get("P", 0.0) or 0.0)
    has_projection = bool(gd.get("has_projection", False))

    qp = result.get("quality_profile", {}) or {}
    substance_index = qp.get("substance_index")
    gap = qp.get("gap")
    components = qp.get("components_available", []) or []

    sm = result.get("source_matching", {}) or {}
    unsourced_rate = sm.get("unsourced_rate")

    # Concerns.
    verified_concern = projected > args.projected_threshold
    gap_concern = gap is not None and gap > args.gap_threshold
    unsourced_concern = (
        unsourced_rate is not None and unsourced_rate > args.unsourced_threshold
    )
    any_concern = verified_concern or gap_concern or unsourced_concern

    # Report.
    out = sys.stdout
    print("# Lodestone score report", file=out)
    print(file=out)
    print(f"Work:   {args.work}", file=out)
    print(f"Source: {args.source}", file=out)
    print(file=out)

    print("## Verified / Not verified (Section II)", file=out)
    print(file=out)
    print(f"- Grounded:  {grounded:.0%}", file=out)
    print(f"- Framed:    {framed:.0%}", file=out)
    print(f"- Projected: {projected:.0%}", file=out)
    print(f"- Has projection flag: {has_projection}", file=out)
    if verified_concern:
        print(f"- **Status: CONCERN** (projected rate > {args.projected_threshold:.0%})", file=out)
        print(
            "  The work projects beyond what the source supports. A claim of done here "
            "would carry projection that the Verified / Not verified rubric (Section II) "
            "requires be made explicit.",
            file=out,
        )
    else:
        print(f"- Status: within threshold (projected rate <= {args.projected_threshold:.0%})", file=out)
    print(file=out)

    print("## Quality theater (Section V)", file=out)
    print(file=out)
    if substance_index is not None and gap is not None:
        print(f"- Substance index: {substance_index:.2f}", file=out)
        print(f"- Gap (presentation minus substance): {gap:+.2f}", file=out)
        if gap_concern:
            print(f"- **Status: CONCERN** (gap > {args.gap_threshold:+.2f})", file=out)
            print(
                "  Presentation runs ahead of substance. This is the measurement symptom "
                "of Quality theater (Section V): claims of quality without the substance "
                "to back them.",
                file=out,
            )
        else:
            print(f"- Status: within threshold (gap <= {args.gap_threshold:+.2f})", file=out)
    else:
        print(f"- Quality profile not available; components: {components}.", file=out)
        print(
            "  Layer 10 requires sufficient text to compute; see Touchstone Standard "
            "Section 5.10 for threshold conditions.",
            file=out,
        )
    print(file=out)

    print("## Assumption over verification (Section V)", file=out)
    print(file=out)
    if unsourced_rate is not None:
        print(f"- Unsourced rate: {unsourced_rate:.0%}", file=out)
        if unsourced_concern:
            print(f"- **Status: CONCERN** (unsourced rate > {args.unsourced_threshold:.0%})", file=out)
            print(
                "  A substantial fraction of claims lack support in the source. This is "
                "the measurement symptom of Assumption over verification (Section V).",
                file=out,
            )
        else:
            print(f"- Status: within threshold (unsourced rate <= {args.unsourced_threshold:.0%})", file=out)
    else:
        print("- Source matching not available for this work.", file=out)
    print(file=out)

    print("## Default implementation (Section VI)", file=out)
    print(file=out)
    print("- Layer 1a baseline-document generation is not run by this script.", file=out)
    print(
        "  To compare against an LLM-generated baseline, invoke Touchstone with the "
        "Layer 1a optional flag; see Touchstone Standard Section 5.1a.",
        file=out,
    )
    print(file=out)

    print("## Summary", file=out)
    print(file=out)
    if any_concern:
        print("**At least one concept tripped a concern threshold.** See sections above.", file=out)
    else:
        print("All measurable concepts within thresholds.", file=out)
    print(file=out)
    print("Concept mapping: see tools/lodestone-via-touchstone.md.", file=out)

    return 1 if any_concern else 0


if __name__ == "__main__":
    sys.exit(main())
