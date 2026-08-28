const whatsapp = '56962489780';

document.querySelectorAll('[data-box]').forEach((button) => button.addEventListener('click', () => {
  const value = button.dataset.box;
  const select = document.querySelector('#box');
  [...select.options].forEach((option) => {
    if (option.textContent.startsWith(value)) select.value = option.value;
  });
  document.querySelector('#pedido')?.scrollIntoView({ behavior: 'smooth' });
}));

document.querySelector('#order-form').addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(event.currentTarget);
  const message = [
    'Hola, quiero hacer un pedido en Carnes El Convento.',
    '',
    `Box: ${data.get('box')}`,
    `Modalidad: ${data.get('delivery')}`,
    `Nombre comprador: ${data.get('buyer')}`,
    `Nombre receptor: ${data.get('receiver')}`,
    `Dirección: ${data.get('address')}, ${data.get('commune')}`,
    `Teléfono: ${data.get('phone')}`,
    `Correo: ${data.get('email') || 'No indicado'}`,
    `Fecha preferida: ${data.get('date')}`,
    `Ventana horaria preferida: ${data.get('time') || 'Sin preferencia'}`,
    `Observaciones: ${data.get('notes') || 'Sin observaciones'}`,
    'Pago del despacho: mediante link de Mercado Pago después de confirmar la ruta',
    'Pago del box: al momento de recibirlo',
    'Habrá una persona disponible para recibir y pagar el box: Sí',
    '',
    'Quedo atento a la fecha disponible, ventana horaria y valor del despacho.',
  ].join('\n');
  window.open(`https://wa.me/${whatsapp}?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
});

document.querySelector('.subscribe').addEventListener('submit', (event) => {
  event.preventDefault();
  const phone = event.currentTarget.querySelector('input').value.trim();
  const message = `Hola, quiero recibir promociones y consejos de Carnes El Convento. Mi WhatsApp es ${phone || 'este número'}.`;
  window.open(`https://wa.me/${whatsapp}?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
});
