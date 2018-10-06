const net =require('net');

if(process.argv.length!=4){
    console.log('Two arguments,functions and number,a are needed')
    process.exit()


}
let fun = process.argv[2]
let num=Math.abs(parseInt(process.argv[3]))

//The server is in our machine
let client = net.connect({port:9000},
    function(){
        console.log('Client connected')
        let request ={"fun":fun,"num":num}
        client.write(JSON.stringify(request))


    })

    client.on('data',function(data){

        console.log(data.toString())
        client.end()

    })

    client.on('end',function(){console.log('Client discconnected')})
    client.on('error',function(){console.log('Some connection error')})
    