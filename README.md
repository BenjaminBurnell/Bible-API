# 📖 Bible REST API

## Overview

**Bible REST API** is a lightweight and open-source web service that allows anyone to access Bible text by **version**, **book**, **chapter**, or **verse** through a simple RESTful interface.  
It retrieves data directly from [BenjaminBurnell/Bible](https://github.com/BenjaminBurnell/Bible) — ensuring accuracy and easy version updates — and is powered by **FastAPI** for fast, reliable performance.

---

## Live API

**Base URL**  
➡️ [https://bible-api-5jrz.onrender.com](https://bible-api-5jrz.onrender.com)

**Interactive API Docs (Swagger UI)**  
📘 [https://bible-api-5jrz.onrender.com/docs](https://bible-api-5jrz.onrender.com/docs)

---

## Features

- **Version Support** — Access different Bible translations (e.g., KJV, WEBUS).  
- **Verse Lookup** — Fetch any verse using `/verse/{version}/{book}/{chapter}/{verse}`.  
- **Chapter Retrieval** — Get full chapters with `/chapter/{version}/{book}/{chapter}`.  
- **GitHub JSON Integration** — Bible data is stored and versioned directly in GitHub.  
- **CORS-Enabled** — Safe for frontend and browser-based use.  
- **Free & Public** — Anyone can use the API with no authentication required.

---

## How It Works

The API dynamically fetches structured JSON files stored in GitHub.  
Each Bible version is organized by book and chapter, for example:

```
bible_data/
└── KJV/
    └── GEN/
        ├── 1.json
        ├── 2.json
```

When a request is made:
1. FastAPI routes the query (e.g. `/verse/KJV/GEN/1/1`).
2. The corresponding JSON is fetched from GitHub.  
3. The specific verse or chapter is returned as a clean JSON response.

---

## Example Usage

### Get a Verse
```
GET /verse/KJV/GEN/1/1
```
**Response:**
```json
{
  "version": "KJV",
  "book": "GEN",
  "chapter": 1,
  "verse": 1,
  "text": "In the beginning God created the heaven and the earth."
}
```

### Get a Chapter
```
GET /chapter/KJV/GEN/1
```

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/BenjaminBurnell/Bible-API
cd Bible-API
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
uvicorn main:app --reload
```

Then open your browser:
```
http://127.0.0.1:8000/docs
```

---

## Built With

- **Python 3.x** — Core programming language  
- **FastAPI** — Web framework for creating REST APIs  
- **Uvicorn** — ASGI server for high-speed performance  
- **Requests** — Fetches Bible JSON data from GitHub  
- **Render** — Free hosting for public deployment  

---

## Future Enhancements

- Add **/search** endpoint to find verses by keyword.  
- Include **cross-version comparison** (e.g., KJV vs WEBUS).  
- Support **daily verse randomizer** endpoint.  
- Add optional **GraphQL** interface for flexible queries.  
- Cache frequently accessed chapters to speed up response times.

---

## License

MIT License © 2025 **Benjamin Burnell**

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

## Credits

Developed by **Benjamin Burnell**  
Data sourced from the public [Bible repository](https://github.com/BenjaminBurnell/Bible).  
Powered by **FastAPI**, **Render**, and the Word of God.

> _"The grass withereth, the flower fadeth: but the word of our God shall stand for ever."_  
> — Isaiah 40:8
