from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI(
    title="Bible REST API",
    description="Fetch Bible data directly from the GitHub repo.",
    version="1.4.0"
)

GITHUB_BASE_URL = "https://raw.githubusercontent.com/BenjaminBurnell/Bible/main/bible_data"

BOOK_CODES = {
    "GENESIS": "GEN", "EXODUS": "EXO", "LEVITICUS": "LEV", "NUMBERS": "NUM", "DEUTERONOMY": "DEU",
    "JOSHUA": "JOS", "JUDGES": "JDG", "RUTH": "RUT", "1 SAMUEL": "1SA", "2 SAMUEL": "2SA",
    "1 KINGS": "1KI", "2 KINGS": "2KI", "1 CHRONICLES": "1CH", "2 CHRONICLES": "2CH",
    "EZRA": "EZR", "NEHEMIAH": "NEH", "ESTHER": "EST", "JOB": "JOB", "PSALMS": "PSA",
    "PROVERBS": "PRO", "ECCLESIASTES": "ECC", "SONG OF SOLOMON": "SNG", "ISAIAH": "ISA",
    "JEREMIAH": "JER", "LAMENTATIONS": "LAM", "EZEKIEL": "EZK", "DANIEL": "DAN", "HOSEA": "HOS",
    "JOEL": "JOL", "AMOS": "AMO", "OBADIAH": "OBA", "JONAH": "JON", "MICAH": "MIC", "NAHUM": "NAM",
    "HABAKKUK": "HAB", "ZEPHANIAH": "ZEP", "HAGGAI": "HAG", "ZECHARIAH": "ZEC", "MALACHI": "MAL",
    "MATTHEW": "MAT", "MARK": "MRK", "LUKE": "LUK", "JOHN": "JHN", "ACTS": "ACT", "ROMANS": "ROM",
    "1 CORINTHIANS": "1CO", "2 CORINTHIANS": "2CO", "GALATIANS": "GAL", "EPHESIANS": "EPH",
    "PHILIPPIANS": "PHP", "COLOSSIANS": "COL", "1 THESSALONIANS": "1TH", "2 THESSALONIANS": "2TH",
    "1 TIMOTHY": "1TI", "2 TIMOTHY": "2TI", "TITUS": "TIT", "PHILEMON": "PHM", "HEBREWS": "HEB",
    "JAMES": "JAS", "1 PETER": "1PE", "2 PETER": "2PE", "1 JOHN": "1JN", "2 JOHN": "2JN",
    "3 JOHN": "3JN", "JUDE": "JUD", "REVELATION": "REV"
}

@app.get("/verse/{version}/{book}/{chapter}/{verse}")
def get_verse(version: str, book: str, chapter: int, verse: int):
    """Fetch a single verse (based on your JSON structure)."""
    version = version.upper()
    book = book.upper()
    book_code = BOOK_CODES.get(book, book)
    
    url = f"{GITHUB_BASE_URL}/{version}/{book_code}/{chapter}.json"
    res = requests.get(url)
    if res.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Chapter not found at {url}")
    
    try:
        data = json.loads(res.text)
        verses = data.get("verses", [])
        for v in verses:
            if str(v.get("verse")) == str(verse):
                return {
                    "version": version,
                    "book": book_code,
                    "chapter": chapter,
                    "verse": verse,
                    "text": v.get("text")
                }
        raise HTTPException(status_code=404, detail="Verse not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error parsing JSON")


@app.get("/chapter/{version}/{book}/{chapter}")
def get_chapter(version: str, book: str, chapter: int):
    """Fetch an entire chapter (returns the 'verses' array)."""
    version = version.upper()
    book = book.upper()
    book_code = BOOK_CODES.get(book, book)
    
    url = f"{GITHUB_BASE_URL}/{version}/{book_code}/{chapter}.json"
    res = requests.get(url)
    if res.status_code != 200:
        raise HTTPException(status_code=404, detail=f"Chapter not found at {url}")
    
    try:
        data = json.loads(res.text)
        return {
            "version": data.get("version", version),
            "book": data.get("book", book_code),
            "chapter": data.get("chapter", chapter),
            "verses": data.get("verses", [])
        }
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error parsing JSON")
