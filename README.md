# Parakram GATE 2026 📚

A personal study dashboard for the **Parakram GATE 2026** batch by Physics Wallah — covering all CS & IT subjects with video lectures, class notes, and daily practice problems (DPPs).

---

## Features

- **19 Subjects** — COA, OS, CN, DS, Algorithms, DBMS, Compiler Design, TOC, Digital Logic, Discrete Math, Linear Algebra, Calculus, Probability & Statistics, C Programming, and more
- **Video Player** — Direct Google Drive streaming with multi-URL fallback and an embedded iframe as a last resort
- **Notes & DPPs** — Per-lecture class notes and chapter-level DPP PDFs/videos accessible with one click
- **Progress Tracking** — Mark lectures as done; progress persists via `localStorage`
- **Global Search** — Fuzzy search across all lectures, chapters, and subjects (`Ctrl+K` / `⌘K`)
- **Keyboard Navigation** — Arrow keys to navigate chapters on the lectures page
- **Responsive UI** — Works on desktop, tablet, and mobile

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML, CSS, JavaScript |
| Fonts | Plus Jakarta Sans (Google Fonts) |
| Video | HTML5 `<video>` + Google Drive streaming |
| Hosting | Hugging Face Spaces (Gradio + FastAPI) |
| Storage | Browser `localStorage` for progress |

---

## Project Structure

```
.
├── app.py          # FastAPI + Gradio server (serves static files)
├── index.html      # Single-page application shell
├── style.css       # All styles (dark theme, responsive)
├── script.js       # All logic — routing, player, search, data
└── README.md
```

---

## How It Works

### Video Playback
Videos are hosted on Google Drive. The player attempts five different CDN/export URLs in sequence before falling back to the Drive embed iframe. If all streaming methods fail, it offers download and local file playback options.

### Data
All subject, chapter, and lecture data (Google Drive file IDs for videos and notes) is defined directly in `script.js` as plain JavaScript objects — no backend or API calls required.

### Progress
Lecture completion state is stored in `localStorage` under the key `parakram_progress` and reflected in per-subject progress bars and the global stats overview.

---

## Subjects Covered

| # | Subject | Code |
|---|---|---|
| 1 | Computer Organization & Architecture | COA |
| 2 | Operating Systems | OS |
| 3 | Computer Networks | CN |
| 4 | Data Structures & Programming | DS |
| 5 | Algorithms | ALGO |
| 6 | Database Management System | DBMS |
| 7 | Compiler Design | CD |
| 8 | Theory of Computation | TOC |
| 9 | Digital Logic | DL |
| 10 | Discrete Mathematics | DM |
| 11 | Linear Algebra | LA |
| 12 | Calculus & Optimization | CALC |
| 13 | Probability & Statistics | PROB |
| 14 | C Programming | C |
| 15 | Fundamentals of C Language | FC |
| 16 | Foundation of Engineering Math | FEM |
| 17 | General Aptitude | GA |
| 18 | Verbal Aptitude | VA |
| 19 | Basics of Computer System | BCS |

---

## Running Locally

```bash
pip install gradio fastapi uvicorn
python app.py
```

Then open `http://localhost:7860` in your browser.

---

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+K` / `⌘K` | Open global search |
| `Esc` | Close search / modal |
| `→` | Next chapter (on Lectures page) |
| `←` | Previous chapter (on Lectures page) |

---

*Parakram GATE 2026 Batch · Physics Wallah*
