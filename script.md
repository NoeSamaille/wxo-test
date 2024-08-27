# Demo script

## Introduce the use case - 1 min

Arguments:
- We all work on projects.
- We have great tooling to track progress, identify blockers, collaborate on open items and so on.
- What if we can go a bit further?
  - Automatically come up with user stories targeted to optimize user experience, access management, functionality, usability, and overall system performance.
  - Automatically identify risks given a current status of a project and suggest a remediation plan.
  - Automatically summarize current state of a project, what's been done in the current sprint, each sprint, etc.
- Let's build an AI assistant to do just that using watsonx.ai and watsonx Orchestrate.

## Create prompt for User Story generation - 1 min

Go to watsonx.ai SaaS, start building a prompt then copy content of [prompt.txt](./prompt.txt).

## Develop a basic FastAPI server for User Story generation - 3 min

1. Create a python script and edit with Continue: 
    ```
    Generate a FastAPI skeleton protected with basic API key that loads environment variables from .env file and exposes /health and /user-stories/generate endpoints.
    ```
2. Copy the code from watsonx to that file.
3. Ask continue to generate a Dockerfile for the codebase.

## Build and deploy FastAPI server to Code Engine - 2 min

1. Build the Dockerfile in Code Engine.
2. Run the app.
3. Test the running app in Code Engine.

## Create watsonx Orchestrate skill to integrate that API - 3 min

TODO

## Show the more advanced demo - 5 min
