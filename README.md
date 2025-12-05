# Build an AI-powered Shopping Catalog with SerpApi's Bing Copilot API and Shopping API

Code examples for blog post: Build an AI-powered Shopping Catalog with SerpApi's Bing Copilot API and Shopping API

You can read the blog post here: https://serpapi.com/blog/build-an-ai-powered-shopping-catalog-with-serpapi-and-python/

---

**Getting Started With Using SerpApi**

You can use our APIs in multiple languages, but for the purposes of this blog post, I've used Python.

To begin scraping data, first, create a free account on serpapi.com. You'll receive 250 free search credits each month to explore the API.

Get your SerpApi API Key from this page: https://serpapi.com/manage-api-key. 

Set your API key in an environment variable, instead of directly pasting it in the code. For this tutorial, I have saved the API key in an environment variable named "SERPAPI_API_KEY" in my .env file. [Optional but Recommended]

Next, on your local computer, you need to install a couple libraries:

`pip install -r requirements.txt`

---

**Run The Code**

Head to the project folder and run the code file using `python buying_catalog_builder.py`

---

**Sample Output**

For a persona_query: 

```
"Christmas gift ideas for a tech savvy teenager in 2025 who likes smart home gadgets and gaming"
```

The resulting CSV looks like this:

<img width="904" height="258" alt="Screenshot 2025-12-02 at 5 01 11 PM" src="https://github.com/user-attachments/assets/482c50f9-4c58-4709-b844-9ffa295eddec" />

