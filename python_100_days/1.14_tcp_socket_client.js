// TCP 客户端
const net = require('net');
const client = net.createConnection({ host: '127.0.0.1', port: 3001 }, () => {
    // 'connect' listener.
    console.log('connected to server!');
    // client.write('world!\r\n');
});
client.on('data', (data) => {
    console.log(data.toString());
    client.end();
});
client.on('end', () => {
    console.log('disconnected from server');
});
