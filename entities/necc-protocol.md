---
slug: "necc-protocol"
title: "Necc Protocol"
oneliner: "Inverse perps backed by an interest bearing stablecoin and bonds."
website: "https://www.necc.io/"
twitter: "https://twitter.com/neccdao"
medium: "https://neccdao.medium.com/"
discord: "https://discord.com/invite/jUcjEauuvw"
github: "https://github.com/neccdao"
logo: /img/necc-protocol.jpg
category: app, defi, aurora
---

Necc is a yield-bearing, fully collateralised stablecoin protocol. These properties are achieved by creating delta neutral positions on whitelisted collaterals. Deposited collateral is lent out to long and short traders to create up to 50x leveraged positions. Fees from trading and liquidations accrue to the stablecoin minters via a second token, NECC.

NECC can also be vested by selling NDOL or NDOL/nNECC LP tokens to the Treasury.

The stablecoin, NDOL, can be minted by depositing a whitelisted collateral. This stablecoin is minted 1-1 to the collateral's USD value, per its associated Flux oracle price feed. NDOL can be burned for any whitelisted collateral type at a rate of (collateral in pool) / (supply of NDOL).

Traders looking to open leveraged positions can "borrow", or more accurately, trade against the collateral pool, with up to 50x leverage. A trader can deposit 1 ETH, then borrow 1 more ETH, for a total position size of 2 ETH.

NDOL retains its value against trading by seizing the long and short traders' collateral when price volatility occurs, and by natural price appreciation when prices rise.