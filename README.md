# Python Coursework — Music Store & Mark Entry System

Two first-year university Python coursework projects demonstrating file I/O, data validation, modular design, and iterative development from procedural scripts through to Jupyter notebook interfaces.

---

## Project 1: Music Store Rental Management System

A menu-driven music store application that manages a catalogue of physical music media (vinyl, CD, tape), handles rentals and returns, enforces subscription-tier rental limits (Basic: 2, Premium: 7), and stores customer feedback. The system interfaces with pre-compiled `subscriptionManager` and `feedbackManager` modules.

**Data files:**
- `Music_Info.txt` — catalogue (RecordID, Artist, Title, Medium, Genre, PurchaseDate)
- `Subscription_Info.txt` — customer subscriptions with tier and validity dates
- `Rental.txt` — active rentals
- `Music_Feedback.txt` — customer ratings and comments

**Key source files:**
- `Music_Store_Files/menu.ipynb` — main interactive notebook interface
- `MusicSearch(2).py` — catalogue search
- `MusicRent.py` — rental processing
- `MusicReturn.py` — return processing
- `checkSubscribed.py` — subscription validation
- `ValidateRID.py` — record ID validation

### Running

Open `Music_Store_Files/menu.ipynb` in Jupyter and run all cells. Python 3.10+ required.

```bash
jupyter notebook "Music_Store_Files/menu.ipynb"
```

---

## Project 2: Mark Entry System

A student mark management system that reads, validates, updates, and reports on student marks stored in a flat text file. The project was developed across five iterations (V1 through V5), progressing from a single-file script to a modular design with separated file operations and a Jupyter notebook front-end.

**Key source files:**
- `Mark Entry System/MainV4_V5/Menuv5.ipynb` — final notebook version
- `Mark Entry System/mainV3/mainV3.py` — last pure-Python version
- `Mark Entry System/mainV3/fileOperation.py` — extracted file I/O module
- `Mark Entry System/mainV1/mainv1.py` — first iteration (single file)

### Running

```bash
jupyter notebook "Mark Entry System/MainV4_V5/Menuv5.ipynb"
```

---

## What I learned

Building the same functionality across five versions of the mark entry system showed clearly how separating concerns (extracting `fileOperation.py` in V3) makes the code easier to reason about and test. Working with flat-file persistence without a database forced me to think carefully about data consistency — what happens if a rental record and a catalogue record disagree, and how to validate inputs before writing. The Jupyter notebook interface made the application more approachable but introduced its own discipline: cells need to be runnable in order and state needs to be predictable between runs.
