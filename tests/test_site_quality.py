from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class SiteQualityTests(unittest.TestCase):
    def test_has_social_and_canonical_metadata_for_production_domain(self):
        self.assertIn('rel="canonical" href="https://www.carneselconvento.cl/"', HTML)
        self.assertIn('property="og:title"', HTML)
        self.assertIn('property="og:description"', HTML)
        self.assertIn('property="og:image"', HTML)

    def test_uses_optimized_webp_images(self):
        webp_images = [
            "hero-parrilla.webp",
            "box-parrillero.webp",
            "box-familiar.webp",
            "box-sandwich-producto.webp",
            "familia-parrilla.webp",
            "don-constantino.webp",
            "logo-mejorado.webp",
        ]
        for image in webp_images:
            self.assertTrue((ROOT / image).is_file(), f"Missing optimized image: {image}")
        self.assertIn('hero-parrilla.webp', CSS)
        self.assertIn('loading="lazy"', HTML)
        self.assertIn('decoding="async"', HTML)


if __name__ == "__main__":
    unittest.main()
