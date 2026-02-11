<#
run_pairs.ps1

Purpose:
Batch orchestrates metadata extraction and comparison between original
DOC/DOCX files and converted PDF/A files.

Responsibilities:
- Iterates through original files
- Calls ExifTool to generate per-file metadata CSVs
- Invokes compare_single_row_csvs.py for field-level comparison
- Writes results to a structured output directory

Parameters:
- origDir: Path to original DOC/DOCX files
- pdfDir: Path to converted PDF/A files
- workDir: Path where metadata CSVs and results are stored
- pythonScriptPath: Path to compare_single_row_csvs.py

Assumptions:
- Filenames match between originals and converted files
- ExifTool is available in system PATH
#>


param(
  [Parameter(Mandatory=$true)][string]$origDir,
  [Parameter(Mandatory=$true)][string]$pdfDir,
  [Parameter(Mandatory=$true)][string]$workDir,
  [Parameter(Mandatory=$true)][string]$pythonScriptPath
)

New-Item -ItemType Directory -Force -Path $workDir | Out-Null
$metaOrigDir = Join-Path $workDir "meta_word_csv"
$metaPdfDir  = Join-Path $workDir "meta_pdf_csv"
$pairDir     = Join-Path $workDir "pair_comparisons"
New-Item -ItemType Directory -Force -Path $metaOrigDir, $metaPdfDir, $pairDir | Out-Null

$masterCsv = Join-Path $workDir "MASTER_metadata_comparison.csv"
if (Test-Path $masterCsv) { Remove-Item $masterCsv }

$wordFiles = Get-ChildItem -LiteralPath $origDir -File | Where-Object { $_.Extension -in ".doc", ".docx" }

foreach ($w in $wordFiles) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($w.Name)
    $pdfPath = Join-Path $pdfDir ($base + ".pdf")

    if (-not (Test-Path -LiteralPath $pdfPath)) {
        Write-Warning "No matching PDF found for: $($w.Name)"
        continue
    }

    $origCsv = Join-Path $metaOrigDir ($base + ".word.csv")
    $pdfCsv  = Join-Path $metaPdfDir  ($base + ".pdf.csv")
    $pairCsv = Join-Path $pairDir     ($base + ".compare.csv")

    # 1) Extract metadata to single-row CSVs (no wildcards)
    exiftool -csv -a -G1 -s $w.FullName   | Set-Content -Encoding utf8 $origCsv
    exiftool -csv -a -G1 -s $pdfPath      | Set-Content -Encoding utf8 $pdfCsv

    # 2) Compare the two CSVs -> long comparison CSV
    python $pythonScriptPath --orig_csv $origCsv --conv_csv $pdfCsv --base_name $base --out_csv $pairCsv

    # 3) Append to master
    if (-not (Test-Path $masterCsv)) {
        Copy-Item $pairCsv $masterCsv
    } else {
        Import-Csv $pairCsv | Export-Csv $masterCsv -NoTypeInformation -Append
    }

    Write-Host "✅ Done: $base"
}

Write-Host "ALL DONE."
Write-Host "Master comparison CSV: $masterCsv"
