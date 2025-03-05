import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    AUTHORITY = os.getenv("AUTHORITY")  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # TODO: Enter your application client ID here
    CLIENT_ID = os.getenv("CLIENT_ID")

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = os.getenv("REDIRECT_PATH")  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = os.getenv("SCOPE")

    SESSION_TYPE = os.getenv("SESSION_TYPE") # So token cache will be stored in server-side session