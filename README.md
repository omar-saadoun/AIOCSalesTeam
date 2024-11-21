# Mysalesteam Crew

Welcome to the Mysalesteam Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv

pip install git+https://github.com/pinnace/py-near.git
pip install git+https://github.com/pvolnov/py-near.git

```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/mysalesteam/config/agents.yaml` to define your agents
- Modify `src/mysalesteam/config/tasks.yaml` to define your tasks
- Modify `src/mysalesteam/crew.py` to add your own logic, tools and specific args
- Modify `src/mysalesteam/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the MySalesTeam Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The MySalesTeam Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Mysalesteam Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

New account <omar3.testnet> created successfully.

--------------------  Access key info ------------------
                                
Master Seed Phrase: hair salute outer island scene scare lend bargain foot train decrease mosquito
Seed Phrase HD Path: m/44'/397'/0'
Implicit Account ID: efff2d84c4368225b5b794fb74d55d6924512f09915adf13b4df81d0519a46e1
Public Key: ed25519:H9r7yj9V5jiNPsXNA2ixAmcK2i9RqgpoWpL6RYPdeF2g
SECRET KEYPAIR: ed25519:R8VPRGkS127sqW15BGEUrPC8GLc6Z7LDwa6p8yuwaKVLBJbjmf1oKZYkmNcBWoak7VuQfWrNW2H251DKf7ppLji
                                
--------------------------------------------------------

Transaction ID: 8uUGZxSgudZMRUpdSvsGd2PCbQC6Y4hng2DU9wTvaseL
To see the transaction in the transaction explorer, please open this url in your browser:
https://explorer.testnet.near.org/transactions/8uUGZxSgudZMRUpdSvsGd2PCbQC6Y4hng2DU9wTvaseL


Here is your console command if you need to script it or re-run:
    near account create-account sponsor-by-faucet-service omar3.testnet autogenerate-new-keypair print-to-terminal network-config testnet create

