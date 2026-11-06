# Project Proposal: Fast-Lane Forward Error Correction (FEC) for Automated Toll Booths

## 1. Project Overview
**Context:** In automated toll plazas, vehicles moving at 20-40 km/h transmit RFID tags and payment IDs to Roadside Units (RSUs). 
**Problem:** Heavy metallic environments cause electrical noise, leading to bit flips. Standard Stop-and-Wait ARQ (retransmission) causes unacceptable latency, resulting in traffic bottlenecks.
**Solution:** Implement an In-Place Error-Correcting Link Layer using Forward Error Correction (FEC) like Hamming Codes to mathematically locate and fix bit flips on the fly, eliminating the need for retransmissions.

## 2. Academic Relevance (Undergraduate Level)
*   **Computer Networks:** Directly applies Data Link Layer concepts (Error Detection/Correction vs. Flow Control).
*   **Algorithms & Mathematics:** Translates theoretical error-correcting polynomials/matrices into applied logic.
*   **Systems Programming:** Involves low-level bitwise manipulation and socket programming.

## 3. Implementation Strategy (1-Week Software Simulation)
To complete this within a week in short sessions, the project will be built as a **network simulation** rather than a physical hardware deployment.

### Tech Stack
*   **Language:** C (Standard C99/C11)
*   **Networking:** UDP Sockets (UDP is connectionless and does not guarantee delivery, making it perfect for simulating raw, noisy link-layer frames).

### Architecture Components
1.  **Vehicle Client (Sender):** 
    *   Takes a simulated License Plate or FastTag ID (hex string).
    *   Encodes the data using a Hamming(7,4) or Hamming(15,11) algorithm using bitwise operations.
    *   Transmits the packet via UDP.
2.  **Noisy Channel (Intermediary/Simulator):**
    *   Intercepts the UDP packet.
    *   Introduces artificial noise (randomly flipping 1 bit based on a configurable probability).
    *   Forwards the corrupted packet to the receiver.
3.  **Toll Gate Server (Receiver):**
    *   Receives the packet.
    *   Runs the Hamming decoder algorithm.
    *   Detects the error, mathematically locates the flipped bit, and corrects it in memory.
    *   Logs the successful extraction of the ID.

## 4. Development Milestones
*   **Session 1: The Core Algorithm.** Write pure C functions for `encode_hamming()` and `decode_and_correct_hamming()`. Test locally with static hex strings.
*   **Session 2: Sockets & Communication.** Wrap the logic in a simple UDP Client-Server architecture. Send encoded payloads from client to server.
*   **Session 3: The Noise Simulator.** Add the randomization logic to flip bits before the server receives the packet. Ensure the server successfully corrects it.
*   **Session 4: Benchmarking & Logging.** Create formatting to print the raw hex strings, show the flipped bit in red (optional terminal colors), and log the processing time (latency) in milliseconds to prove it is faster than an ARQ timeout.

## 5. Presentation & Deliverables
*   **Live Demo:** Side-by-side terminal windows showing the Sender, the Noisy Channel, and the Receiver successfully correcting the ID without requesting a re-send.
*   **Metrics:** A simple comparison table showing the latency of a simulated ARQ retransmission vs. the sub-millisecond FEC correction.
