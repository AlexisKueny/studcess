from openrouter import OpenRouter
from dotenv import load_dotenv
from supabase import create_client, Client
import os

# Load environment variables
load_dotenv()

# Open router config
open_router_client = OpenRouter(api_key=os.getenv("OPENROUTER_SDK_KEY")) 
print(open_router_client)

# Supabase config
supabase_client = create_client(
    os.getenv("VECTOR_DB_URL"),
    os.getenv("VECTOR_DB_KEY")
)
print(supabase_client)