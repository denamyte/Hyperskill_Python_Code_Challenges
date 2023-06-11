def submit_data(data, client, address):
    with client:
        client.connect(address)
        client.send(data.encode())
