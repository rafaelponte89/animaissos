

//classe central da API usada para criar o mapa
var mapao = L.map('map', { center: [-20.718637820756296, -47.880477905273445], zoom: 17 })

//carrega camadas de apresentação sobre o mapa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapao);

let elemento = document.getElementsByClassName('leaflet-control-container');

elemento[0].classList.add('fixed-top');