#!/bin/bash
# A script return the size of the response
curl -so /dev/null $1 -w '%{size_download}\n'
