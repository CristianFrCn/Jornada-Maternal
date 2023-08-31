from googleapiclient.discovery import build

GOOGLE_API_KEY = 'AIzaSyCz0lYYs-QUmyqYx0xIIDeJrf6oSxWk9_M'
GOOGLE_CSE_ID = '47069417be7bc44e8'

def google_custom_search(query):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    result = service.cse().list(q=query, cx=GOOGLE_CSE_ID).execute()
    return result.get('items', [])
