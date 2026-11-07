# BareBones Project | Static verification and geometry tests
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class WireframeTests(unittest.TestCase):
    def test_name_and_credits(self):
        self.assertIn("space-geometric-wireframe", HTML)
        self.assertIn('class="signature"', HTML)
        self.assertIn("BareBones Project", HTML)

    def test_every_project_file_signed(self):
        paths = [
            ROOT / "index.html",
            ROOT / "README.md",
            ROOT / "LICENSE",
            ROOT / ".gitignore",
            ROOT / ".github/workflows/tests.yml",
            ROOT / "tests/test_static.py",
            ROOT / "tests/browser_smoke.py",
        ]
        for path in paths:
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertTrue(path.is_file())
                self.assertIn("BareBones Project", path.read_text(encoding="utf-8"))

    def test_hypercube_geometry(self):
        vertices = [[1 if i >> bit & 1 else -1 for bit in range(4)] for i in range(16)]
        edges = [(i, j) for i in range(16) for j in range(i + 1, 16)
                 if ((i ^ j) & ((i ^ j) - 1)) == 0]
        self.assertEqual(len(vertices), 16)
        self.assertEqual(len(edges), 32)
        self.assertTrue(all(sum(x != y for x, y in zip(vertices[i], vertices[j])) == 1
                            for i, j in edges))

    def test_controls_and_canvas(self):
        for marker in ('id="scene"', 'id="pause"', 'id="speed"', 'id="reset"'):
            with self.subTest(marker=marker):
                self.assertIn(marker, HTML)

    def test_standalone(self):
        self.assertNotIn("<iframe", HTML.lower())
        self.assertNotIn("<script src=", HTML.lower())
        self.assertNotIn("http://", HTML.lower())
        self.assertNotIn("https://", HTML.lower())

    def test_accessibility(self):
        self.assertIn('aria-label="BareBones Project signature"', HTML)
        self.assertIn('aria-label="Animation controls"', HTML)
        self.assertIn("touch-action:none", HTML)


if __name__ == "__main__":
    unittest.main()
