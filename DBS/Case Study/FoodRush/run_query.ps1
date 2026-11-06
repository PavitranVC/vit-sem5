param([Parameter(Mandatory=$true)][int]$Num)
$file = Join-Path $PSScriptRoot ("q{0:D2}.js" -f $Num)
if (-not (Test-Path $file)) { Write-Error "No such file: $file"; exit 1 }
if (-not $env:MONGO_URI) { Write-Error "MONGO_URI is not set"; exit 1 }
$text = Get-Content $file -Raw
Write-Host "===== Source: $(Split-Path $file -Leaf) =====" -ForegroundColor Cyan
Write-Host $text
Write-Host "===== Result =====" -ForegroundColor Cyan
# Wrap the final query statement in printjson(...toArray()); the q file itself stays unchanged.
$lines = $text -split "\r?\n"
$setup = $lines[0]
$query = ($lines[1..($lines.Count-1)] | Where-Object { $_ -notmatch '^\s*//' }) -join "`n"
$query = $query.Trim().TrimEnd(';')
$tmp = Join-Path $env:TEMP ("run_q{0:D2}.js" -f $Num)
Set-Content -Path $tmp -Value "$setup`nprintjson(($query).toArray());" -Encoding utf8
mongosh $env:MONGO_URI --quiet --file $tmp
$code = $LASTEXITCODE
Remove-Item $tmp -ErrorAction SilentlyContinue
exit $code
