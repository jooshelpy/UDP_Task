# UDP Packet Exchange Example

This repository contains a simple example of how to exchange packets using UDP between a server and a client. The client sends packets with incremental numbers, and the server receives and acknowledges them then sends required packet.

## Prerequisites

Make sure you have Python installed on your machine. The code examples provided are compatible with Python 3.

## Files

- 'server.py': Contains the server-side code for sending packets to the client using UDP.
- 'client.py': Contains the client-side code for requesting and receiving packets from the server using UDP.

## Notes

- This is a basic example for educational purposes. In real-world applications, additional error handling and reliability mechanisms would be needed.
- UDP does not guarantee delivery or order of messages. Additional considerations should be made if reliability is a requirement.
- This example does not cover scenarios like dropped packets or network errors. In production, handling such scenarios is crucial.