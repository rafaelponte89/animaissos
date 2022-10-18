carregaPontos();
function carregaPontos() {
    var myIcon = L.icon({
        iconUrl: '/media/fotos_animais/house_5050.png',
        iconSize: [50, 50],
        iconAnchor: [-20, -40],
        popupAnchor: [50, 50],
    });

    // Pega coordenadas da div
    var obj = coord.innerHTML;

    if (obj !== '') {
        // converte para objeto
        const obj_json = JSON.parse(obj);
        //carrega ponto no mapa
        for (let i in obj_json.pontos) {
            L.marker([parseFloat(obj_json.pontos[i].lat), parseFloat(obj_json.pontos[i].long)], { icon: myIcon })
                .addTo(mapao)
                .bindPopup('Título Ponto: ' + obj_json.pontos[i].ponto + "<br>"
                    + 'Qtd Animais: ' + obj_json.pontos[i].qtd_animais);
            //.openPopup();
        }
    }
}