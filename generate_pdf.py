"""Utility script to build the documentation and export it as a PDF.

This script wraps the MkDocs build process and ensures that the
`mkdocs-with-pdf` plugin is activated. When invoked it will build
the documentation site into the default ``site`` directory and
produce a single PDF file at the location configured in
``mkdocs.yml`` (``pdf/dpm-xl-documentation.pdf``). The script
sets the ``ENABLE_PDF_EXPORT`` environment variable to ``1`` before
running the build so that the plugin knows it should generate the
PDF.

Usage:
    python generate_pdf.py [--site-dir <output_directory>]

The optional ``--site-dir`` argument can be used to specify a
different output directory for the generated site and PDF. If
omitted, MkDocs defaults to building into the ``site`` directory.

This file is executable and can be run directly from the command
line on systems with Python installed.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Build the MkDocs site and export it to a single PDF using "
            "the mkdocs-with-pdf plugin."
        )
    )
    parser.add_argument(
        "--site-dir",
        dest="site_dir",
        default=None,
        help=(
            "Directory where the built documentation should be output. "
            "Defaults to the standard 'site' directory if not provided."
        ),
    )
    return parser.parse_args(argv)


def build_documentation(site_dir: str | None) -> None:
    """Run mkdocs to build the site and produce the PDF."""
    env = os.environ.copy()
    # Signal to the mkdocs-with-pdf plugin that PDF generation should run.
    env["ENABLE_PDF_EXPORT"] = "1"

    cmd = ["mkdocs", "build"]
    if site_dir:
        cmd.extend(["--site-dir", site_dir])

    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd, env=env)
    print("\nDocumentation and PDF generation complete.")


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    build_documentation(args.site_dir)


if __name__ == "__main__":
    main()
