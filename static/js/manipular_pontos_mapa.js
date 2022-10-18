
var item = new Array();

// cria o ponto sobre o mapa e abre janela modal
mapao.on("dblclick", function (event) {
    if (item.length < 1) {

        item.push(L.marker(event.latlng).addTo(mapao));
        mostrarCoordenadas();
        $('#exampleModalCenter').modal('show');


    }
    else {
        alert("Somente é possível " + item.length + " coordenada(s) por vez!")
    }


});

// coloca as coordenadas no text input
function mostrarCoordenadas() {

    for (i = 0; i < item.length; i++) {
        let lat = item[i]._latlng.lat.toString();
        let lon = item[i]._latlng.lng.toString();
        latitude.value = lat;
        longitude.value = lon;
    }
}

// // Deleta primeira coordenada do mapa
function deletarPonto() {

    if (item.length !== 0) {
        mapao.removeLayer(item.shift());
        mostrarCoordenadas();
        //  modalCordenada.close();
        limparCampos();
    }
}

function gravarPonto() {
    document.getElementById('coordenadas').submit();

}