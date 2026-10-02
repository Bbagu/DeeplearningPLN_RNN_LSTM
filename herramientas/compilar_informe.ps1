param([string]$TexBin = (Join-Path $env:APPDATA 'TinyTeX\bin\windows'))
$ErrorActionPreference = 'Stop'
$projectDir = Split-Path -Parent $PSScriptRoot
$reportDir = Join-Path $projectDir 'informe'
$pdfLatex = Join-Path $TexBin 'pdflatex.exe'
$bibTex = Join-Path $TexBin 'bibtex.exe'
foreach ($tool in @($pdfLatex, $bibTex)) {
    if (-not (Test-Path -LiteralPath $tool)) { throw "No se encontro la herramienta: $tool" }
}
Push-Location -LiteralPath $reportDir
try {
    & $pdfLatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
    if ($LASTEXITCODE -ne 0) { throw 'Fallo la primera pasada de pdfLaTeX.' }
    & $bibTex main
    if ($LASTEXITCODE -ne 0) { throw 'Fallo BibTeX.' }
    1..2 | ForEach-Object {
        & $pdfLatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
        if ($LASTEXITCODE -ne 0) { throw 'Fallo una pasada final de pdfLaTeX.' }
    }
    Write-Output "PDF generado: $reportDir\main.pdf"
} finally {
    Pop-Location
}
