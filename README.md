# Python Coursework

Two first-year university Python projects. The music store handles rentals and returns for physical media; the mark entry system manages student grades across five versions showing how the code evolved from a single script to a modular notebook interface.

## Project 1: Music Store Rental Management System

A menu-driven application for a music store that rents out physical media (vinyl, CD, tape). Handles rentals and returns, enforces subscription-tier limits (Basic: 2 items, Premium: 7), and stores customer feedback. Interfaces with pre-compiled `subscriptionManager` and `feedbackManager` modules.

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

```bash
jupyter notebook "Music_Store_Files/menu.ipynb"
```

Python 3.10+ required.

## Project 2: Mark Entry System

A student mark management system that reads, validates, updates, and reports on student marks stored in a flat text file. Developed across five iterations (V1 through V5), starting from a single-file script and ending with a modular design and Jupyter notebook front-end.

**Key source files:**
- `Mark Entry System/MainV4_V5/Menuv5.ipynb` — final notebook version
- `Mark Entry System/mainV3/mainV3.py` — last pure-Python version
- `Mark Entry System/mainV3/fileOperation.py` — extracted file I/O module
- `Mark Entry System/mainV1/mainv1.py` — first iteration

### Running

```bash
jupyter notebook "Mark Entry System/MainV4_V5/Menuv5.ipynb"
```

## What I learned

Having five versions of the mark entry system made it clear how much easier the code became once file I/O was pulled into its own module. Flat-file persistence without a database forced me to think about consistency: what happens when a rental record exists but the catalogue entry doesn't match, and how to validate before writing rather than after. Moving to a Jupyter notebook interface also introduced its own discipline around cell ordering and keeping state predictable between runs.
