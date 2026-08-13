const whatsapp = '56939115958';
document.querySelectorAll('[data-box]').forEach((button) => button.addEventListener('click', () => {
  const value = button.dataset.box;
  const select = document.querySelector('#box');
  [...select.options].forEach((option) => { if (option.textContent.startsWith(value)) select.value = option.value; });
}));
document.querySelector('#order-form').addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(event.currentTarget);
  const message = `Hola, quiero hacer un pedido en Carnes El Convento.%0A%0ABox: ${data.get('box')}%0ADespacho: ${data.get('delivery')}%0ANombre comprador: ${data.get('buyer')}%0ANombre receptor: ${data.get('receiver')}%0ADirección: ${data.get('address')}, ${data.get('commune')}%0ATeléfono: ${data.get('phone')}%0ACorreo: ${data.get('email') || 'No indicado'}%0AFecha: ${data.get('date')}%0AHorario aproximado: ${data.get('time')}%0AObservaciones: ${data.get('notes') || 'Sin observaciones'}`;
  window.open(`https://wa.me/${whatsapp}?text=${message}`, '_blank', 'noopener');
});
document.querySelector('.subscribe').addEventListener('submit', (event) => { event.preventDefault(); window.open(`https://wa.me/${whatsapp}?text=Hola,%20quiero%20recibir%20promociones%20y%20consejos%20de%20Carnes%20El%20Convento.`, '_blank', 'noopener'); });
