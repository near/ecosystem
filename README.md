<img src="https://repository-images.githubusercontent.com/384455580/fc80d841-e285-4238-981d-c40e45772469" alt="near-logo" width="600" border="0" />

This repository is the data source for the community-sourced, core team curated NEAR Ecosystem page.

**You can also use [this form](https://nearprotocol1001.typeform.com/submit-project) to submit a project to this database.**

Our aim is to curate an accurate, up-to-date database of all entities in the NEAR ecosystem. Therefore, we have made this an open, community-driven repo which anyone can contribute to.

This is a living, breathing document and repo that will evolve over time as the community helps to maintain the map going forward.

# How To Contribute & Guidelines

We want to ensure the submission process captures as much information as possible pertaining to the entities added, while also remaining straightforward to contribute. 

All submissions to the NEAR Ecosystem are composed of two files: a Markdown file (.md), and a .svg or .png image. 

Adding a new entity to the ecosystem page only consists of two simple steps:
1. Create both a new markdown file in the `entities` directory with headers pertaining to each data field, and a detailed description of the entity outside the table
2. Add a new .svg or .png logo image in the `img` directory. (To upload a .png logo - 1. Fork  2. Upload  3. Create PR)


<b>Logo Submission Guidelines</b>

All .svg/.png files must be 100x100px. Do not embed any excessive raster image files: svg file sizes over 500kb will be rejected.

Below is an example submission for Skyward Finance:

```
---
slug: "skyward-finance"
title: "Skyward Finance"
oneliner: "Enable fair token distribution and price discovery for projects built on NEAR Protocol."
website: "https://skyward.finance/"
app: "https://app.skyward.finance/"
whitepaper: "https://skyward.finance/whitepaper/"
twitter: "https://twitter.com/skywardfinance"
telegram: "https://t.me/skywardfinance"
discord: "https://discord.gg/KKjQwCRvbV"
medium: "https://medium.com/nearprotocol/everything-you-need-to-know-about-skyward-finance-before-the-first-token-sale-6e82fe305e1a"
github: "https://github.com/skyward-finance/"
ticker: "SKYWARD"
logo: /img/skywardfinancelogo.png
category: defi, app
status: launched
contract: skyward.near
---

“Detailed description... (Up to 350 characters max)”

```


### Markdown Headers

Below are the available markdown headers for adding entities with guidelines for each header (only input what is applicable for what you are adding):

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
- `category`: A comma separated list of categories describing the project, see below for accepted list
- `status`: 'building', 'launched', 'mainnet', 'testnet'
- `contract`: Project contract id
- `jobs`: Jobs available
- `community asks`: What they could use help with from community?


### Categories

Available classifications for 'category' header:
Please add multiple tags if needed and include the header category as well.

| infrastructure | ecosystem | defi | funding | nft | gaming | app | guild | partner * |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| exchange | education | amm | accelerator | marketplace |  |  | geographical | 
| oracle | guild | dex | vc |  |  |  | validator |
| wallet | marketing | stablecoin | grants |  |  |  | ecosystem project |
| validator | devshop | lending |  |  |  |  | awareness |
| indexer | social | derivatives |  |  |  |  | theme based guild |
| analytics | utility |
| tools | dao |
| payments |

* 'partner' classification for if $NEAR is used on other networks for something
