# Network Port Scanner

A Python port scanner that checks a target host for open ports and tries to guess what's running on them, using multithreading so it doesn't take forever.

## Why I made this

I'm a CS major at UVA doing the Cybersecurity Focal Path, and wanted something hands-on to actually build instead of just reading about networking concepts. Port scanning is one of the first things you learn about in security. It's literally step one of figuring out what's exposed on a network, so I figured it was a good first project.

## What it does

- Scans a range of ports on a target and tells you which ones are open
- Uses a pool of worker threads (100 by default) pulling from a shared queue instead of spinning up a thread per port — way faster, and doesn't choke your system on bigger scans
- Matches open ports against a list of common ones (22 = SSH, 80 = HTTP, etc.) so you get a rough idea of what's actually running
- Times out on unresponsive ports instead of hanging
- Everything's configurable from the command line — target, port range, thread count

## How to run it

```bash
# scan localhost, ports 1-1024 (defaults)
python3 port_scanner.py 127.0.0.1

# pick your own range
python3 port_scanner.py 127.0.0.1 --start 1 --end 9000

# more threads = faster (usually)
python3 port_scanner.py 127.0.0.1 --threads 200
```

| Flag | What it does | Default |
|------|--------------|---------|
| `target` | IP or hostname to scan | required |
| `--start` | first port to check | 1 |
| `--end` | last port to check | 1024 |
| `--threads` | how many worker threads to run | 100 |

## How it actually works

All the ports in your range get loaded into a queue. Then a fixed number of worker threads grab ports off that queue one at a time and try connecting to each one. If the connection goes through, the port's open. Each connection attempt has a short timeout so one dead port doesn't hold up the whole scan.

Any open port gets checked against a small dictionary of common services, so you're not just staring at a bunch of numbers.

## What I might add later

- Banner grabbing (reading the little "hello" message some services send when you connect)
- Saving results to a file
- UDP support (right now it's TCP only)

## built with

Just Python's standard library (`socket`, `threading`, `queue`, `argparse`)