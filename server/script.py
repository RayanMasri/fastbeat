import uvicorn

async def app(scope, receive, send):
    # Accept WebSocket from browser
    await send({
        'type': 'websocket.accept',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    # Send message to browser
    await send({
        'type': 'websocket.send',
        'text': 'hello'
    })

    # Receive message from browser
    response = await receive()
    print(response)


if __name__ == "__main__":
    uvicorn.run("script:app", host="localhost", port=3000, log_level="info")