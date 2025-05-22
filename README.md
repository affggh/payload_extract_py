# payload_extract_py
Extract payload.bin via bin/zip/url with multithreads

# Requirements
`protobuf` for unmarshall payload struct data    
`rich` for show progress and log    
`requests` for extract payload from url

# Usage
```
usage: payload_extract [-h] [-t {zip,bin,url}] [-T thread] -i input [-o outdir] [-X boot,system,vendor...]

extract zip/bin/url payload.bin

options:
  -h, --help            show this help message and exit
  -t, --type {zip,bin,url}
                        type of input
  -T, --thread thread   workers
  -i, --input input     input file path
  -o, --outdir outdir   output directory
  -X, --extract-partitions boot,system,vendor...
                        extract partitions, split with ','
```
