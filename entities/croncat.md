---
slug: "croncat"
title: "Croncat"
oneliner: "Decentralized Scheduling for Blockchain Transactions"
website: "https://cron.cat/"
app: "https://cron.cat/"
whitepaper: "https://docs.cron.cat/docs/values-vision/"
twitter: "https://twitter.com/croncats"
discord: "https://discord.gg/srxjjwPH"
github: "https://github.com/Cron-Near/"
logo: /img/croncatlogo.png
category: app, ecosystem, infrastructure, tools, utility
status: testnet
contract: "manager.croncat.near"
jobs: "Jobs available"
---

Croncat provides a general purpose, fully autonomous network that enables scheduled function calls for blockchain contract execution. It allows any application to schedule logic to get executed in the future, once or many times, triggered by an approved “agent,” in an economically stable format. Croncat is launching on NEAR Protocol and will initially schedule function calls in $NEAR Token. Future integrations with other NEP-141 tokens are planned.

    Cron is the missing functionality required for contracts to operate as a fully autonomous entity.

How Croncat Works In A Nutshell

Croncat is a looping runtime that maintains a registry of tasks & agents. In the Croncat system, there are two fundamental ‘Stakeholders’:

  * Applications: Blockchain contracts or dApps that schedule future tasks.
  * Agents: Users that execute cron tasks and receive rewards

Tasks that are scheduled by applications or contracts, get put into future buckets which remain dormant until a bucket is active. A bucket becomes active when the block height has been reached or surpassed. Agents communicate with the cron contracts, watching for available tasks & signing transactions that are ready to execute. Agents earn a small reward every time they successfully execute a task.

Many contract functionalities need an extra execution step to enable the completion of some action or state finalization. Without a cron-style execution, contracts on chain must rely on externally provided state & function changes via transactions sent by chain participants. This is a critical logic piece that is innefficient and sometimes expensive for the participant. Such execution could be paid for by the contract (if desired) or made to execute with less logic (cheaper) by not needing to alter large amounts of chain storage.

[Learn more about Use Cases](https://docs.cron.cat/docs/use-cases)

