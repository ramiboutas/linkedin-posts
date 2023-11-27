import os
import dotenv

dotenv.load_dotenv(".env")


# organization or person
author_type = "person"
# LINKEDIN_ORGANIZATION_ID or LINKEDIN_PROFILE_ID
author_id = os.environ.get("LINKEDIN_PROFILE_ID")
# LINKEDIN_ORGANIZATION_ACCESS_TOKEN or LINKEDIN_ACCESS_TOKEN
access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
