//Event Emitter

const Evento =require("./generadorEventos");

const evento1='e1';
const evento2='e2';
var incremento=0;
const emisor1=Evento(evento1,'emisor1:',0);
const emisor2=Evento(evento2,'emisor2 :',"");

function visualizar(entidad,evento,dato){
    console.log(entidad,evento+'..>',dato);

    emisor1.on(visualizar);
    emisor2.on(visualizar);
}

emisiones();{

    function randomm(x=2,y=6){
        return Math.floor(Math.random()*(6-2)+2)

    }
setInterval(visualizar.emisor1,randomm);
setInterval(visualizar.emisor2,randomm);



}