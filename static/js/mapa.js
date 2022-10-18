function limparCampos() {
  latitude.value = '';
  longitude.value = '';
  id_titulo.value = '';
  id_casa.value = '';
  id_protetor.value = '';
  id_qtd_animais.value = '';
}
limparCampos();
//classe central da API usada para criar o mapa
var mapao = L.map('map', { center: [-20.718637820756296, -47.880477905273445], zoom: 17 })


//carrega camadas de apresentação sobre o mapa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapao);

var item = new Array();

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

//mostra coordenadas sobre o mapa no formato lat, long como entradas somente leitura
function mostrarCoordenadas() {
  // //  var entradas = "";
  // //  for (i=0; i<item.length; i++){
  // //      let lat =item[i]._latlng.lat.toString();
  // //      let lon = item[i]._latlng.lng.toString();
  // //      entradas = entradas + "<input type='text' value="+lat+" name='coords"+ lat +"' readonly/>";
  // //      entradas = entradas + "<input type='text' value="+lon+" name='coords"+ lon+"' readonly/>";
  // //      entradas = entradas +"<input type='text' name='descCoords"+ i.toString()+"' placeholder='Endereço do Ponto'/> <br>";
  // // 		  console.log(item[i]._latlng);
  // //  }
  // //
  // //  coordenadas.innerHTML = entradas + "<input type='submit'>";
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


// //        // formata objeto JSON
// //        for (i =0; i < texto.length; i++){
// //            if (( i != 0) && ( i != (texto.length-1)) ){
// //                if (texto[i] === '\'') {
// //
// //                    obj = obj + '\"';
// //                 }
// //                else {
// //                    obj = obj + texto[i];
// //                }
// //            }
// //        }


// carregaPontos();

// function carregaPontos(){

//         // Pega coordenadas da div
//         var obj = coord.innerHTML;

//         if (obj !== ''){
//             // converte para objeto
//             const obj_json = JSON.parse(obj);
//             //carrega ponto no mapa
//             for (let i in obj_json.pontos){
//                L.marker([parseFloat(obj_json.pontos[i].lat), parseFloat(obj_json.pontos[i].long)],{fillColor:'green'})
//                .addTo(mapao)
//                .bindPopup(obj_json.pontos[i].trajeto + '\n' + 
//                obj_json.pontos[i].hr + ':' + obj_json.pontos[i].min);
//                //.openPopup();
//             }
//         }
// }

var myIcon = L.icon({
  iconUrl: '/media/fotos_animais/house_5050.png',
  iconSize: [50, 50],
  iconAnchor: [50, 50],
  popupAnchor: [-50, -76],
});

L.marker([-20.718637820756296, -47.880477905273445], { icon: myIcon }).addTo(mapao);
var popup = L.popup()
  .setLatLng([-20.718637820756296, -47.880477905273445])
  .setContent('<p>Hello world!<br />This is a nice popup.</p>')
  .openOn(mapao);

function gravarPonto() {
  document.getElementById('coordenadas').submit();

}


