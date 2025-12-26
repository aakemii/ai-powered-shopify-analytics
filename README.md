# AI-Powered Shopify Analytics App

An AI-powered analytics system that allows Shopify store owners to ask natural-language business questions and receive clear, layman-friendly insights.

This project demonstrates system design, API architecture, agentic AI workflows, and ShopifyQL reasoning with a clean separation between backend services.

## Project Overview

The application allows users to ask business questions such as:

What were my top selling products last week?  
How much inventory should I reorder for next week?  
Which customers placed repeat orders in the last 90 days?

The system processes these questions by understanding intent, deciding what Shopify data is required, generating ShopifyQL-style queries, processing results, and returning easy-to-understand business explanations.

## Architecture Overview

Client or API consumer sends a request.

Rails API acts as the backend gateway.

Python AI service performs reasoning and analytics.

Shopify API and ShopifyQL serve as the data source (mocked).

## Responsibility Split

Rails API handles request validation, routing, and response formatting.

Python AI service handles intent detection, query planning, ShopifyQL generation, execution logic, and explanation.

Shopify acts as the analytics data source and is mocked for this assignment.

## Agentic Workflow

The Python AI service follows a structured agent-based workflow.

First, the system identifies the intent of the user question, such as sales, inventory, or customers.

Second, it plans which Shopify entities and metrics are required.

Third, it generates a valid ShopifyQL-style query.

Fourth, it executes or simulates the query and processes the results.

Finally, it converts technical metrics into simple, business-friendly insights.

## Tech Stack

Backend Gateway  
Ruby on Rails (API-only)

AI Service  
Python with FastAPI

Agent Logic  
Modular Python components

Authentication  
Shopify OAuth (conceptual and mocked)

## Project Structure

ai-powered-shopify-analytics  
rails-api  
python-ai-service  
agent  
sample-requests  
README.md  

## API Example

Request

POST /ask

JSON body

{
  "store_id": "demo.myshopify.com",
  "question": "What were my top selling products last week?"
}

Response

{
  "answer": "This is a mock AI response",
  "confidence": "medium"
}

## Running the Python AI Service

Navigate to the python-ai-service directory.

Install dependencies using:

python -m pip install -r requirements.txt

Run the server using:

python -m uvicorn main:app --reload

Open the browser and visit:

http://127.0.0.1:8000/docs

Use the Swagger UI to test the API endpoint.

## Assumptions and Mocks

Shopify OAuth authentication is mocked.

ShopifyQL execution is simulated.

LLM reasoning is rule-based for clarity and explainability.

These components can be replaced with real implementations without changing the overall architecture.

## Error Handling

The API validates input strictly using schemas.

Invalid or malformed requests return clear error responses.

The system handles incomplete or ambiguous questions gracefully.

## Future Improvements

Real Shopify OAuth integration.

Live ShopifyQL execution.

LLM integration using OpenAI, Claude, or Gemini.

Conversation memory for follow-up questions.

Caching and analytics dashboard.

## Author

Pratyush Sharma  
GitHub: https://github.com/aakemii

## Status

Project completed.


