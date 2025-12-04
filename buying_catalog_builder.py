import re
from serpapi import GoogleSearch
import os, csv 
from dotenv import load_dotenv
load_dotenv()

def generate_ideas_with_bing_copilot(query):
    params = {
    "engine": "bing_copilot",
    "q": query,
    "api_key": os.environ["SERPAPI_API_KEY"]
    }

    search = GoogleSearch(params)
    result = search.get_dict()
    return result

def get_shopping_results_with_bing_shopping_and_write_to_csv(gifts_suggested_by_bing_copilot):
    for gift in gifts_suggested_by_bing_copilot:
        params = {
        "engine": "bing_shopping",
        "q": gift,
        "api_key": os.environ["SERPAPI_API_KEY"]
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        if results.get('shopping_results'):
            result = results['shopping_results'][0]
        with open("bing_shopping_results.csv", "a", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([result.get('title'), result.get('external_link'), result.get('price'), result.get('seller')])

if __name__ == "__main__":
    # Define the persona
    persona_query = "Christmas gift ideas for a tech savvy teenager in 2025 who likes smart home gadgets and gaming"
    
    copilot_result = generate_ideas_with_bing_copilot(persona_query)

    header = ["title", "external_link", "price", "seller"]
    with open("bing_shopping_results.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

    gifts_suggested_by_bing_copilot = []
    for item in copilot_result.get("text_blocks", []):
        if item.get("type") == "list":
            for bullet in item.get("list", []):
                snippet = bullet.get("snippet", [])
                #Bing often formats the gift idea with a dash or colon after the main idea
                gift_idea = re.split(r'[–:]', snippet, maxsplit=1)[0].strip()
                gifts_suggested_by_bing_copilot.append(gift_idea)
    
    shopping_result = get_shopping_results_with_bing_shopping_and_write_to_csv(gifts_suggested_by_bing_copilot)



