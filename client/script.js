console.log('hi');

let ws = new WebSocket('ws://localhost:3000/');

ws.onopen = () => {
    console.log('open');
    ws.send(Array.from({ length: 10000 }, (x, i) => i).join(''));
};

ws.onmessage = (event) => {
    console.log(event.data);
};
