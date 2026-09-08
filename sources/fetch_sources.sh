#!/usr/bin/env bash
# Re-download the public Pantheon+ release files used in this audit and verify SHA-256 against sources/manifest.csv values.
set -euo pipefail
cd "$(dirname "$0")"
B="https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR"
[ -f "Pantheon+SH0ES.dat" ] || curl -sS -o "Pantheon+SH0ES.dat" "$B/Pantheon%2BSH0ES.dat"
[ -f "Pantheon+SH0ES_STAT+SYS.cov" ] || curl -sS -o "Pantheon+SH0ES_STAT+SYS.cov" "$B/Pantheon%2BSH0ES_STAT%2BSYS.cov"
sha256sum -c SHA256SUMS.txt
