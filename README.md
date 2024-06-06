# djangocon-eu-2024-workshop

This is a quick example of using code carbon to run serverside code and get energy usage figures.

The goal is demonstrate running a local piece of code, and having some insight into the power used

https://mlco2.github.io/codecarbon/


### Set up a virtual environment


```
python -m venv .venv
```

### Activate it

```
source .venv/bin/activate
```

### Install the python dependencies

```
python -m pip install -r requirements.in

```

### Fetch something that uses a bunch of server-side compute

This will use the installed `llm` package to fetch a local LLM, and then run a test prompt

```
llm install llm-gpt4all
llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'
```

## Run some code

```
python ./example-code-carbon.py
```
