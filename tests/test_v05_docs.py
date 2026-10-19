"""Keep public capability and quick-start guidance consistent with shipped files."""
import re
import unittest
from pathlib import Path

from src.va import core, methodology


class DocumentationConsistencyTests(unittest.TestCase):
    def test_public_docs_exist_and_local_links_resolve(self):
        for relative in ('README.md', 'ABOUT.md', 'CONTRIBUTING.md', 'vm.py',
                         'docs/GETTING_STARTED.md', 'docs/METHOD_SELECTION.md',
                         'docs/CAPABILITY_STATUS.md', 'docs/PROJECT_POSITIONING.md'):
            path = core.ROOT / relative
            self.assertTrue(path.is_file(), relative)
            content = path.read_text(encoding='utf8')
            for url in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
                if url.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                target = (path.parent / url.split('#', 1)[0]).resolve()
                self.assertTrue(target.is_file(), f'{relative}: bad reference to {url}')

    def test_public_inventory_not_stale(self):
        readme = (core.ROOT / 'README.md').read_text(encoding='utf8')
        actual_skills = sum(1 for p in (core.ROOT / 'skills').iterdir() if (p / 'SKILL.md').is_file())
        actual_methods = len(methodology.load_catalog())
        self.assertRegex(readme, rf'\b{actual_skills} original (?:portable )?skill')
        self.assertRegex(readme, rf'\b{actual_methods} (?:cataloged )?methods')
        self.assertTrue('cannot yet conduct independent research' in readme or
                        'does **not** yet perform autonomous research' in readme)
        self.assertIn('Brad Khan', readme)
        self.assertIn('Venture Method', readme)


if __name__ == '__main__':
    unittest.main()
