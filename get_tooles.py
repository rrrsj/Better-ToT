def get_tools(retiver=None,k=None):
    tooles = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location.",
            "parameters": {
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                },
            },
        },
        {
            "name": "get_forecast_weather",
            "description": "Get the forecast weather in a given location.",
            "parameters": {
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "days":{
                        "type":"number",
                        "description":"The time want to get of future weather."
                    }
                },
            },
        },
        {
            "name": "get_location",
            "description": "Get the latitude and longitude of the location based on the address name. ",
            "parameters": {
                "properties": {
                    "address": {
                        "type": "string",
                        "description": "The specific address, e.g. San Francisco, CA", 
                    },
                },
                },
        },
        {
            "name":'get_nearby_places',
            "description": "Search for locations near the current location. It can be used to find specific places, e.g., restaurants and schools. You should obtain the user's position firstly.",
            "parameters": {
                "properties": {
                    "location": {
                        "type": "string", 
                        "description": "the name of the current location.", 
                        },
                    "radius": {
                        "type": "number", 
                        "description": "Radius from current position.", 
                        },
                    "keyword": {
                        "type": "string", 
                        "description": "Keywords of the query, e.g., restaurants and schools.", 
                        },
                },
                },
        },
        {
            "name":"get_route",
            "description": "Inquire about routes between the two locations.",
            "parameters": {
                "properties": {
                    "origin": {
                        "type": "string", 
                        "description": "the start of the route.", 
                        },
                    "destination": {
                        "type": "string", 
                        "description": "the end of the route.", 
                        },
                },
                },
        },
        {
            "name":"get_distance",
            "description": "Check the distance between two places.",
            "parameters": {
                "properties": {
                    "origin": {
                        "type": "string", 
                        "description": "the start of the route.", 
                        },
                    "destination": {
                        "type": "string",
                        "description": "the end of the route.", 
                        },
                },
                },
        },
    ]
    if retiver==None:
        return tooles
        
