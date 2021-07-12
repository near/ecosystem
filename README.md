<a href="https://ibb.co/QrPc0n8"><img src="https://i.ibb.co/r4xt9Mb/near-logo.png" alt="near-logo" border="0" /></a>

# NEAR Ecosystem

This repository is the data source for the NEAR Ecosystem page, located at [near.org/ecosystem](https://near.org/ecosystem).

# Contributing Guidelines

All integrations in the NEAR Ecosystem are composed of two files: a Markdown file with headers, and an .svg or .png image. To add a new project to the ecosystem page, create both a new Markdown file in the `integrations` directory and add a new .svg or .png image in the `img` directory.

### Markdown Headers

```
---
slug: "skyward-finance"
date: "04-01-2021"
title: "Skyward Finance"
oneliner: "Enable fair token distribution and price discovery for projects built on NEAR Protocol."
website: "https://skyward.finance/"
app: "https://app.skyward.finance/"
twitter: "https://twitter.com/skywardfinance"
telegram: "https://t.me/skywardfinance"
discord: "https://discord.gg/KKjQwCRvbV"
medium: "https://medium.com/nearprotocol/everything-you-need-to-know-about-skyward-finance-before-the-first-token-sale-6e82fe305e1a"
github: "https://github.com/skyward-finance/"
logo: /img/skywardfinancelogo.png
integration: project
category: defi, app, launchpad
status: live
contract: "skyward.near"
---
```

Example Markdown headers are above (only input what is applicatble to the integration you are adding). Below are guidelines for each field:

- `slug`: The page URL that follows after near.org/ecosystem/
- `date`: The date of project addition
- `title`: The title of the project
- `oneliner`: The one line summary of the project and its integration to NEAR
- `website`: A URL to direct users to the page
- `app`: A URL directly to the app
- `twitter`: A URL to the twitter page
- `telegram`: A URL to the telegram channel
- `discord`: A URL to the discord channel
- `medium`: A URL to the medium page
- `github`: A URL to the github page
- `token`: 
- `dao`:
- `logo`: A relative path to the corresponding SVG/PNG image
- `integration`: How it ties into the NEAR Ecosystem (see below)
- `category`: A comma separated list of categories describing the project
- `status`: The status of the integration: `live`, `building`, `closed`
- `contract`: Project contract

### Categories

Available classifications for integrations:

```
project
guild
dao
company
fund
accelerator
```


Available classifications for project categories:

```
amm
app
defi
dex
exchange
explorer
infra
oracle
spl
stablecoin
tools
wallet
metaplex
```

### Image Guidelines

All .svg/.png files must be 100x100px. Do not embed any excessive raster image files: svg filesizes over 500kb will be rejected.

