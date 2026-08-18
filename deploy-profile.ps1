# deploy-profile.ps1 — publish the profile README bundle to github.com/muend/muend
#
# Run it from inside your muend/muend working copy:
#   .\deploy-profile.ps1
#   .\deploy-profile.ps1 -Zip C:\path\to\muend-profile.zip
#
# Extracts the bundle over the repo, removes the retired banner, shows the diff,
# asks once, then commits and pushes.

param(
  [string]$Zip = "",
  [string]$Message = "Rewrite profile README as a verified systems index",
  [switch]$Yes
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
  Write-Host "No .git here. cd into your muend/muend working copy first." -ForegroundColor Red
  exit 1
}

if (-not $Zip) {
  $candidate = Get-ChildItem "$HOME\Downloads\muend-profile*.zip" -ErrorAction SilentlyContinue |
               Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if (-not $candidate) {
    Write-Host "No muend-profile*.zip found in Downloads. Pass one with -Zip." -ForegroundColor Red
    exit 1
  }
  $Zip = $candidate.FullName
}
if (-not (Test-Path $Zip)) { Write-Host "Not found: $Zip" -ForegroundColor Red; exit 1 }
Write-Host "Bundle: $Zip" -ForegroundColor Cyan

# GitHub rejects pushes that would expose a private address
$email = git config user.email
if (-not $email -or $email -notmatch "users\.noreply\.github\.com") {
  Write-Host "Setting commit identity to your GitHub noreply address." -ForegroundColor Yellow
  git config user.name  "muend"
  git config user.email "173892601+muend@users.noreply.github.com"
}

git pull --ff-only origin main
Expand-Archive -Path $Zip -DestinationPath . -Force

# the single banner was replaced by a light/dark pair
if (Test-Path "assets\banner.svg") {
  Remove-Item "assets\banner.svg"
  Write-Host "Removed the retired assets\banner.svg." -ForegroundColor Yellow
}

git add -A
$changes = git status --short
if (-not $changes) { Write-Host "Nothing changed. Already up to date." -ForegroundColor Green; exit 0 }

Write-Host ""
Write-Host "Changes to be committed:" -ForegroundColor Cyan
$changes | ForEach-Object { Write-Host "  $_" }

if (-not $Yes) {
  Write-Host ""
  $reply = Read-Host "Commit and push to main? (y/N)"
  if ($reply -ne "y") { Write-Host "Stopped. Nothing was pushed." -ForegroundColor Yellow; exit 0 }
}

git commit -m $Message
git push origin main

Write-Host ""
Write-Host "Pushed. Open https://github.com/muend to check it." -ForegroundColor Green
Write-Host "Toggle GitHub's theme once to confirm the banner swaps." -ForegroundColor Gray
