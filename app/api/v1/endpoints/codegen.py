
from fastapi import APIRouter
router = APIRouter(prefix="/codegen", tags=["Code Generation (12)"])

@router.get("/basic")
def basic(language: str = "python"):
    if language.lower() == "python":
        code = "import pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.describe())"
    elif language.lower() == "r":
        code = "df <- read.csv('data.csv')\nsummary(df)"
    else:
        code = "// Sample code not available for this language yet."
    return {"language": language, "code": code}
