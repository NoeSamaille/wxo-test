# Demo script

## Introduce the use case - 1 min

Imagine this: We all work on projects, and we have fantastic tools to track progress, identify blockers, and collaborate on open items. But what if we could take it a step further? But now Generative AI has oppened a whole new world of possibilities, now we can build robust AI assistants to empower Product Owners to increase their productivity writing down user stories based on product requirements, better prioritize work items and gain insights to make better decisions.

Because I always love a challenge, let's build this AI assistant using watsonx.ai and watsonx Orchestrate in the next 15 minutes.

## Create prompt for User Story generation - 1 min

Go to watsonx.ai SaaS, start building a prompt then copy content of [prompt.txt](./prompt.txt).
2. Create `requirements.txt` file with the following content:
    ```
    fastapi
    uvicorn
    python-dotenv
    langchain-ibm
    ```
3. Improve the script by initializing the `WatsonxLLM` and implement the `/user-stories/generate` endpoint.
4. Test locally.
5. Ask continue to generate a Dockerfile for the codebase.
6. Push to a new public GitHub repo.

## Build and deploy FastAPI server to Code Engine - 2 min

1. Go to Code Engine on IBM Cloud.
2. Create a new application that builds app from GitHub repo.
3. While it's building, create the OpenAPI spec for Orchestrate.
   1. Add the following to the `openapi.yaml` file, replacing server `url` with the right Code Engine endpoint:
      ```
          "openapi": "3.0.0",
          "info": {
              "title": "PMO API NS TEST",
              "version": "0.1.0",
              "description": "Generate User Stories"
          },
          "security": [
              {
                  "APIKeyHeader": []
              }
          ],
          "servers": [
              {
                  "url": "https://pmo-api.1ibjqd27pmzm.eu-de.codeengine.appdomain.cloud"
              }
          ],
      ```
4. Test the running app in Code Engine.

## Create watsonx Orchestrate skill to integrate that API - 3 min

1. On orchestrate, go to skill studio and create a new skill from OpenAPI spec.
2. Test the new skill in chat mode.
3. Create a simple skill flow with that skill and `Create Card` skill from Trello.

## Show the more advanced demo - 5 min

1. Mention that we did all that in 10-12mins
2. Use the last 2-3 minutes to show the more advanced items, including board summarization and project risk analysis.

Thanks for your time!
