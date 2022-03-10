const EventEmitter = require('events')
const eventEmitter = new EventEmitter()

eventEmitter.on('start', () => {
  console.log('first emitter -- started')
})

eventEmitter.on('start', () => {
  console.log('second emitter -- started')
})

eventEmitter.on('stop', () => {
  console.log('first emitter -- stopped')
})

eventEmitter.emit('start', 23)
