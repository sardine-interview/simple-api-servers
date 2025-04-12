const http = require('http');
const server = http.createServer();

server.on('request', (request, response) => {
  let body = [];
  request.on('data', (chunk) => {
    body.push(chunk);
  }).on('end', () => {
    body = Buffer.concat(body).toString();
    response.write(body);
    response.end();
  });
}).listen(8080);

console.log('Server is running on port 8080');