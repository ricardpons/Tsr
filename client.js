const zmq=require('zeromq')

let req=zmq.Socket('req')
let math=require('./myMath')

const fu=process.id
