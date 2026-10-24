"""Bundle the reference library into distributable wheels without duplicating sources in Git.

The source checkout remains canonical. Only read-only reference assets are copied
into the build directory; the original engagement CLI and runtime are not imported.
"""
from pathlib import Path
from shutil import copy2
from setuptools import setup
from setuptools.command.build_py import build_py

REPO = Path(__file__).resolve().parent


class BuildWithReferences(build_py):
    def run(self):
        super().run()
        target_root = Path(self.build_lib) / "src" / "va" / "_library"
        for name in ("config", "skills", "schemas"):
            for source in (REPO / name).rglob("*"):
                if source.is_file() and source.suffix in (".json", ".md"):
                    dest = target_root / source.relative_to(REPO)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    copy2(source, dest)
        for name in ("ADOPT.md", "ABOUT.md", "docs/PORTABLE_ADOPTION.md"):
            dest = target_root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            copy2(REPO / name, dest)


setup(cmdclass={"build_py": BuildWithReferences})
