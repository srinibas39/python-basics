import aiohttp
import json
import asyncio
city = "chennai"
URL = f"https://wttr.in/{city}?format=j1"
async def fetch_weather():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                if response.status != 200:
                    raise Exception("API Error: {response.status}")
                
                data = await response.json()
                print(data["nearest_area"])
                with open("weather.json","w") as f:
                    json.dump(data,f,indent=4)
                return data
    except aiohttp.ClientError as e:
            print(f"❌ Network error: {e}")
    except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
    finally:
            print("✅ Fetch attempt finished.")

async def main():
     weather = await fetch_weather()  

if __name__ == "__main__":
     asyncio.run(main())      
    

