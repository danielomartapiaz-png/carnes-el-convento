from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
JS = (ROOT / "app.js").read_text(encoding="utf-8")


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

    def test_product_cards_include_commercial_decision_details(self):
        self.assertIn('$9.998 CLP/kg aprox.', HTML)
        self.assertIn('$8.748 CLP/kg aprox.', HTML)
        self.assertIn('4 bifes de lomo vetado de 250 g', HTML)
        self.assertIn('1 kg de costillar de cerdo en tira', HTML)
        self.assertIn('1 kg de trutro de pollo', HTML)
        self.assertIn('1 kg de chorizos parrilleros artesanales', HTML)
        self.assertIn('1 kg de churrasco de posta rosada', HTML)
        self.assertIn('1 kg de pechuga de pollo deshuesada', HTML)
        self.assertIn('1 kg de posta molida con 6% M.G., en 4 porciones de 250 g', HTML)
        self.assertIn('5 chuletas de cerdo de 200 g', HTML)
        self.assertIn('1 kg de churrasco de posta rosada (20 unidades)', HTML)
        self.assertIn('1 kg de lomito de cerdo laminado (20 unidades)', HTML)
        self.assertIn('1 kg de hamburguesas artesanales (10 unidades)', HTML)
        self.assertIn('3 kg en total', HTML)
        self.assertIn('$9.997 CLP/kg aprox.', HTML)
        self.assertGreaterEqual(HTML.count('$39.990 CLP'), 2)
        self.assertGreaterEqual(HTML.count('$34.990 CLP'), 2)
        self.assertGreaterEqual(HTML.count('$29.990 CLP'), 2)
        self.assertGreaterEqual(HTML.count('class="product-facts"'), 3)

    def test_delivery_uses_owned_sectorized_routes_and_customer_coordination(self):
        self.assertIn('Despachos programados por sector', HTML)
        self.assertIn('transporte propio', HTML)
        self.assertIn('Agrupamos pedidos de comunas cercanas', HTML)
        self.assertIn('Fecha preferida de entrega', HTML)
        self.assertIn('sujeta a disponibilidad de ruta', HTML)
        self.assertIn('Despacho programado por sector', HTML)
        self.assertNotIn('Quiero consultar una entrega especial', HTML)
        self.assertIn('Valor según comuna y ruta programada', HTML)
        self.assertNotIn('Despacho normal · $3.500 CLP', HTML)
        self.assertNotIn('Despacho express · $6.000 CLP', HTML)
        self.assertNotIn('A todas las comunas de Santiago', HTML)
        self.assertNotIn('Despacho en todo Santiago', CSS)
        self.assertIn('Rutas programadas por sector', CSS)
        self.assertIn('Fecha preferida:', JS)
        self.assertIn('Modalidad:', JS)

    def test_delivery_payment_uses_confirmed_mercado_pago_link_and_requires_reception(self):
        self.assertIn('Pago seguro del despacho', HTML)
        self.assertIn('link de Mercado Pago', HTML)
        self.assertIn('No realices ningún pago antes de recibir nuestra confirmación', HTML)
        self.assertIn('El valor del box se paga al momento de recibirlo', HTML)
        self.assertIn('productos perecibles', HTML)
        self.assertIn('name="reception"', HTML)
        self.assertIn('persona disponible para recibir', HTML)
        self.assertNotIn('href="https://mpago.la/', HTML)
        self.assertIn('Pago del despacho: mediante link de Mercado Pago', JS)
        self.assertIn('Habrá una persona disponible para recibir y pagar el box', JS)

    def test_trust_and_delivery_conditions_are_explicit(self):
        self.assertIn('id="confianza"', HTML)
        self.assertIn('Compra con confianza', HTML)
        self.assertIn('Envasado al vacío', HTML)
        self.assertIn('Confirmamos cualquier reemplazo contigo', HTML)
        self.assertIn('id="condiciones-despacho"', HTML)
        self.assertIn('Hasta las 18:00 del día anterior', HTML)
        self.assertIn('href="#condiciones-despacho"', HTML)

    def test_delivery_conditions_use_grouped_visual_hierarchy(self):
        self.assertIn('class="conditions-header"', HTML)
        self.assertEqual(HTML.count('class="condition-highlight"'), 3)
        self.assertEqual(HTML.count('class="policy-group"'), 4)
        for heading in ('Tu ruta', 'Pago y reserva', 'Recepción del pedido', 'Cambios y contingencias'):
            self.assertIn(f'<h4>{heading}</h4>', HTML)
        self.assertIn('.conditions-summary', CSS)
        self.assertIn('.policy-groups', CSS)
        self.assertNotIn('.delivery-conditions li { padding:', CSS)

    def test_product_card_emphasis_follows_pointer_or_keyboard_focus(self):
        self.assertNotIn('.product-card.featured { outline:', CSS)
        self.assertIn('.product-card:hover, .product-card:focus-within', CSS)
        self.assertIn('outline: 2px solid var(--gold)', CSS)

    def test_brand_character_and_header_assets_are_updated(self):
        self.assertNotIn('Constantino', HTML)
        self.assertNotIn('constantino', HTML)
        self.assertIn('Conventino', HTML)
        self.assertIn('id="conventino"', HTML)
        self.assertIn('conventino-retrato.webp', HTML)
        self.assertIn('familia-parrilla.webp', HTML)
        self.assertIn('logo-icon.webp', HTML)
        self.assertNotIn('🐴', HTML)
        for image in ('conventino-retrato.webp', 'conventino-familia.webp', 'logo-icon.webp'):
            self.assertTrue((ROOT / image).is_file(), f"Missing brand image: {image}")


if __name__ == "__main__":
    unittest.main()
