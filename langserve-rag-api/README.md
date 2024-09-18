# langserve-rag-api

## Local installation

### Install micromamba

If you have acceess to
[mamba](https://mamba.readthedocs.io/en/latest/index.html) via some other
method (maybe you have already installed
[miniforge](https://github.com/conda-forge/miniforge)), you can skip
this step.

Otherwise, install micromamba following
[these instructions](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html#linux-and-macos).

For x86_64 Linux, this would be:

```sh
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
```

Once you have access to `mamba`/`micromamba`, create an environment with
```sh
bin/micromamba env create -f environment.yml
```
when using micromamba or with
```sh
mamba env create -f environment.yml
```
when using mamba.

### Setting up OpenAI API keys

This RAG example utilizes OpenAI compatible endpoint.
You can either launch your own or use any other compatible one.

You can set these via environment variables or through
`secrets/api_keys.env`.

The following keys need to be set:

- `OPENAI_API_KEY`: API key for the OpenAI endpoint
- `OPENAI_BASE_URL`: Base URL for the OpenAI endpoint.
- `OPENAI_MODEL`: Model to use from the OpenAI endpoint.

If you're using API keys from Aalto Azure OpenAI endpoint,
you need to set `AZURE_AUTH=1` as well.

Example secrets are shown in `secrets/example_api_keys.env`.

Remember that you should never share your API keys and you
should never commit your API keys to a repository.

## Starting up the server

Activate the environment with:

```sh
eval "$(./bin/micromamba shell hook -s posix)"
micromamba activate langserve-rag-api
```

When using `mamba`, use either
```sh
mamba activate langserve-rag-api
```
or
```sh
source activate langserve-rag-api
```

Now you can launch the server with
```sh
uvicorn app.server:app --host 0.0.0.0 --port 8080 --reload
```

This will start the server in the reload mode where changes
to the code base will reload the server automatically.

## Testing the different API endpoints

You can go to http://localhost:8080 with your browser to
see the available endpoints.

There are four llm endpoints that you can test out in
their respective playgrounds:

- http://localhost:8080/llm/playground - Direct access to the LLM.
- http://localhost:8080/json/playground/ - LLM that answers the question in a JSON format.
- http://localhost:8080/limerick/playground/ - LLM that answers the question with a limerick in a JSON format.
- http://localhost:8080/salesman/playground/ - LLM that uses RAG functionality to retrieve a random city from a list of three cities and tries to sell you a travel package to said city.
