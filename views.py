from django.contrib import messages
from django.shortcuts import redirect, render

from pruebaDS.conversorMonedas import ConversionMetodoFactory


def conversionMoneda(request):
    """
    Maneja la solicitud para realizar la conversion de monedas
    Proceso:
    Obtiene los datos del form
    - Llama a ConversionMetodoFactory
    - La clase ConversionMetodoFactory devuelve un objeto convertidor_monedas
    - El convertidor_monedas realiza la conversion de las monedas
    - Devuelve la plantila con el resultado de la operacion
    """
    if request.method == 'POST':
        try:
            total_ingresado = request.POST['valorIngresado']
            moneda_inicio = request.POST['unidadOrigen']
            moneda_final = request.POST['unidadDestino']
            moneda_ingresada = request.POST['unidadOrigen']
            convertidor_monedas = ConversionMetodoFactory.getConversion(moneda_ingresada)
            resultado = convertidor_monedas.conversion(total_ingresado, moneda_inicio, moneda_final)
            return render(request, 'ConversionMonedas.html', {'resultado': resultado, 'moneda': moneda_final})
        except ValueError as e:
            return render(request, 'ConversionMonedas.html', {'error': str(e)})
    return render(request, 'ConversionMonedas.html')
