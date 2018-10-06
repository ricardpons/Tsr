const ev=require('events');
const emitter =new ev.EventEmitter();
const e1="print",e2="read";
var n1=0,n2=0;

emitter.on(e1,
    function(){
        console.log('event'+e1+''+n1+++'times')
    })
    
    emitter.on(e2,
        function(){
            console.log('event'+e2+''+n2+++'times')
        })
        
    
        emitter.on(e1,
            function(){
                console.log('Somthing has been printed')
            })

emitter.emit(e1);
emitter.emit(e2);
console.log("--------------------------------");


setInterval(
    function(){
        emitter.emit(e1);
    },2000);

    setInterval(
        function(){
            emitter.emit(e2);
        },8000);
 console.log("\n\t==========>endi of code:eventes become emitted periodically\n");          