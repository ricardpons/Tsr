var ev = require('events');
var emitter = new ev.EventEmitter;
var e1 = "one";
var e2 = "two";
var e3 = "three";
var period=2000;

// Constructor for class Listener.
function Listener() {
  this.num1 = 0;
  this.num2 = 0;
  this.top = false;
}

Listener.prototype.event1 = function() {
  this.num1++;
  console.log( "Active listener." );
}

Listener.prototype.event2 = function() {
  this.num2++;
  if (this.num2 > this.num1)
    console.log( "Event two." );
  else 
    console.log( "I have received more events of type 'one'." );
}

Listener.prototype.event3 = function() {
  console.log( "Event three." );
  if (!this.top) {
      period *= 2;
      if (period > 9000) {
	  period=9000;
	  this.top=true;
	  }
  }
}

// A Listener object is created.
var lis = new Listener();

// Emit event e2 using setTimeout() instead of setInterval().
// This doesn't break the current interval when we 
// extend that interval length.
function emitE2() {
    emitter.emit(e2);
    setTimeout(emitE2, period);
}

// Listener is registered on the event emitter.
emitter.on(e1, function() {lis.event1()});
emitter.on(e2, function() {lis.event2()});
emitter.on(e3, function() {lis.event3()});

// Generate the events periodically...
// First event generated every 3 seconds.
setInterval( function() {
    emitter.emit(e1);
  }, 3000 );
// Second event generated every "period" seconds.
// To this end we call emitE2 instead of emitter.emit(e2).
setTimeout( emitE2, period );
// Third event generated every 10 seconds.
setInterval( function() {
    emitter.emit(e3);
  }, 10000 );


