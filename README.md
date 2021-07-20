<a href="https://ibb.co/QrPc0n8"><img src="https://i.ibb.co/r4xt9Mb/near-logo.png" alt="near-logo" border="0" /></a>

# NEAR Ecosystem

This repository is the data source for the NEAR Ecosystem page, located at [near.org/ecosystem](https://near.org/ecosystem).

# Contributing Guidelines

All submissions to the NEAR Ecosystem are composed of two files: a Markdown file with headers, and an .svg or .png image. To add a new project to the ecosystem page, create both a new Markdown file in the `entities` directory and add a new .svg or .png image in the `img` directory.


### Markdown Headers

```
---
slug: "skyward-finance"
title: "Skyward Finance"
oneliner: "Enable fair token distribution and price discovery for projects built on NEAR Protocol."
website: "https://skyward.finance/"
app: "https://app.skyward.finance/"
twitter: "https://twitter.com/skywardfinance"
telegram: "https://t.me/skywardfinance"
discord: "https://discord.gg/KKjQwCRvbV"
medium: "https://medium.com/nearprotocol/everything-you-need-to-know-about-skyward-finance-before-the-first-token-sale-6e82fe305e1a"
github: "https://github.com/skyward-finance/"
ticker: 
logo: /img/skywardfinancelogo.png
category: defi, app, launchpad
status: live
contract: "skyward.near"
---
```

Example Markdown headers are above (only input what is applicable for what you are adding). Below are guidelines for each field:

- `slug`: The page URL that follows after near.org/ecosystem/
- `title`: The title of the project
- `oneliner`: The one line summary
- `website`: A URL to direct users to the page
- `app`: A URL directly to the app
- `whitepaper`: A URL directly to white/lite paper
- `twitter`: A URL to the twitter page
- `telegram`: A URL to the telegram channel
- `discord`: A URL to the discord channel
- `youtube`: A URL to the YouTube channel
- `medium`: A URL to the medium page
- `github`: A URL to the github page
- `ticker`: Token ticker
- `logo`: A relative path to the corresponding SVG/PNG image
- `category`: A comma separated list of categories describing the project
- `status`: 'building', 'launched', 'inactive'
- `contracts`: Project contracts
- `community asks`: What they could use help with?


### Categories

Available classifications for 'categories':


```
infrastructure
ecosystem
defi
gaming
dao
nft
app
guild
funding
exchange
explorer
oracle
wallet
validator
indexer
analytics
marketplace
tools
education
marketing
devshop
accelerator
vc
grants
amm
launchpad
dex
stablecoin
lending
derivatives
```

### Image Guidelines

All .svg/.png files must be 100x100px. Do not embed any excessive raster image files: svg filesizes over 500kb will be rejected.

