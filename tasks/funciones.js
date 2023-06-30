$(document).ready(function() {
    $('input[type="checkbox"], input[type="radio"], input[type="number"]').on('change', function() {
      // Calcular los totales nuevamente
      var totalServicios = 0;
      var totalEventos = 0;
      var totalAlimentos = 0;
  
      $('input[name="servicios"]:checked').each(function() {
        totalServicios += parseInt($(this).val());
      });
  
      $('input[name="eventos"]:checked').each(function() {
        totalEventos += parseInt($(this).val());
      });
  
      $('input[name="alimentos"]:checked').each(function() {
        totalAlimentos += parseInt($(this).val());
      });
  
      var cantidadPersonas = parseInt($('#Personas').val());
      totalAlimentos *= cantidadPersonas;
  
      var totalGeneral = totalServicios + totalEventos + totalAlimentos;
  
       // Actualizar los valores en la página
    $('#total-servicios').text(totalServicios);
    $('#total-eventos').text(totalEventos);
    $('#total-alimentos').text(totalAlimentos);
    $('#total-general').text(totalGeneral);
  });
});