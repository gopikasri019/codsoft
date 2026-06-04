import tkinter as tk
from tkinter import scrolledtext
import random

# ====================== WINDOW ======================
root = tk.Tk()
root.title("🎵 AI Music Recommendation System")
root.geometry("1400x900")
root.minsize(1200, 800)
root.configure(bg="#EDE9FE")

# ====================== DATA ======================
songs = {
    "blinding lights":{"genre":"pop","mood":"happy","artist":"The Weeknd","rating":4.9},
    "shape of you":{"genre":"pop","mood":"happy","artist":"Ed Sheeran","rating":4.8},
    "stay":{"genre":"pop","mood":"happy","artist":"Justin Bieber","rating":4.7},
    "believer":{"genre":"rock","mood":"energetic","artist":"Imagine Dragons","rating":4.8},
    "thunder":{"genre":"rock","mood":"energetic","artist":"Imagine Dragons","rating":4.7},
    "radioactive":{"genre":"rock","mood":"energetic","artist":"Imagine Dragons","rating":4.8},
    "perfect":{"genre":"romantic","mood":"relaxed","artist":"Ed Sheeran","rating":4.9},
    "night changes":{"genre":"romantic","mood":"relaxed","artist":"One Direction","rating":4.8},
    "senorita":{"genre":"romantic","mood":"happy","artist":"Shawn Mendes","rating":4.7},
    "faded":{"genre":"electronic","mood":"sad","artist":"Alan Walker","rating":4.8},
    "alone":{"genre":"electronic","mood":"energetic","artist":"Alan Walker","rating":4.7},
    "animals":{"genre":"electronic","mood":"energetic","artist":"Martin Garrix","rating":4.8},
    "heat waves":{"genre":"indie","mood":"relaxed","artist":"Glass Animals","rating":4.8},
    "505":{"genre":"indie","mood":"sad","artist":"Arctic Monkeys","rating":4.7},
    "unstoppable":{"genre":"motivational","mood":"energetic","artist":"Sia","rating":4.9},
    "hall of fame":{"genre":"motivational","mood":"energetic","artist":"The Script","rating":4.9},
}

favorites = []
history = []

# ====================== LOGIC ======================
def recommend_genre(g):
    return "🎼 " + g.upper() + " SONGS\n\n" + "\n".join(
        f"• {s.title()} - {i['artist']}"
        for s, i in songs.items() if i["genre"] == g
    )

def recommend_mood(m):
    return "😊 " + m.upper() + " MOOD SONGS\n\n" + "\n".join(
        f"• {s.title()} - {i['artist']}"
        for s, i in songs.items() if i["mood"] == m
    )

def search_song(name):
    for s, i in songs.items():
        if name.lower() in s:
            return f"""🎵 {s.title()}

🎤 Artist: {i['artist']}
🎼 Genre: {i['genre'].title()}
😊 Mood: {i['mood'].title()}
⭐ Rating: {i['rating']}"""
    return "❌ Song not found."

def top_songs():
    ranked = sorted(songs.items(), key=lambda x:x[1]["rating"], reverse=True)
    text = "🏆 TOP SONGS\n\n"
    for n,(s,i) in enumerate(ranked[:5],1):
        text += f"{n}. {s.title()} - {i['artist']} ⭐ {i['rating']}\n"
    return text

def surprise_song():
    return search_song(random.choice(list(songs.keys())))

def get_reply(msg):
    m = msg.lower().strip()

    if m in ["pop","rock","romantic","electronic","indie","motivational"]:
        history.append(m)
        return recommend_genre(m)

    if m in ["happy","sad","energetic","relaxed"]:
        history.append(m)
        return recommend_mood(m)

    if "top" in m:
        return top_songs()

    if "surprise" in m:
        return surprise_song()

    if m == "favorites":
        return "\n".join(favorites) if favorites else "No favorites yet."

    if m == "history":
        return "\n".join(history) if history else "No history yet."

    if m.startswith("add "):
        song = m[4:]
        if song in songs:
            favorites.append(song)
            return f"❤️ Added {song.title()} to favorites."
        return "❌ Song not found."

    return search_song(m)

# ====================== SEND ======================
def send_message():
    msg = entry.get().strip()
    if not msg:
        return

    chat.config(state="normal")
    chat.insert("end", f"\n👤 YOU:\n{msg}\n\n", "user")
    chat.insert("end", f"🤖 AI:\n{get_reply(msg)}\n\n", "bot")
    chat.config(state="disabled")
    chat.yview("end")
    entry.delete(0, "end")

# ====================== TITLE ======================
tk.Label(
    root,
    text="🎵 AI MUSIC RECOMMENDATION SYSTEM",
    font=("Segoe UI", 26, "bold"),
    bg="#EDE9FE",
    fg="#6D28D9"
).pack(pady=15)

# ====================== MAIN ======================
main = tk.Frame(root, bg="#EDE9FE")
main.pack(fill="both", expand=True, padx=10, pady=10)

# Sidebar
left = tk.Frame(main, bg="#F5F3FF", width=380)
left.pack(side="left", fill="y")
left.pack_propagate(False)

menu = """
💜 AI MUSIC BOT

━━━━━━━━━━━━━━━━━━

🎵 Welcome to your Lavender Music Assistant

🎼 GENRES

• pop
• rock
• romantic
• electronic
• indie
• motivational

😊 MOODS

• happy
• sad
• energetic
• relaxed

⭐ FEATURES

• top songs
• surprise me
• add believer
• favorites
• history

🔍 Search any song or artist
"""

tk.Label(
    left,
    text=menu,
    justify="left",
    anchor="nw",
    bg="#F5F3FF",
    fg="#6D28D9",
    font=("Segoe UI", 12)
).pack(fill="both", expand=True, padx=20, pady=20)

divider = tk.Frame(main, bg="#D8B4FE", width=2)
divider.pack(side="left", fill="y", padx=5)

# Right Panel
right = tk.Frame(main, bg="#FAF8FF")
right.pack(side="left", fill="both", expand=True)

tk.Label(
    right,
    text="🎵",
    font=("Segoe UI Emoji", 80),
    bg="#FAF8FF",
    fg="#A855F7"
).pack(pady=(40, 10))

tk.Label(
    right,
    text="How can I help you today?",
    font=("Segoe UI", 24, "bold"),
    bg="#FAF8FF",
    fg="#7C3AED"
).pack()

tk.Label(
    right,
    text="Search for songs, artists, moods or ask for recommendations.",
    font=("Segoe UI", 13),
    bg="#FAF8FF",
    fg="#6B7280"
).pack(pady=10)

chat = scrolledtext.ScrolledText(
    right,
    height=12,
    font=("Segoe UI", 11),
    bg="white",
    fg="#4C1D95"
)
chat.pack(fill="both", expand=True, padx=40, pady=(20,10))

chat.tag_config("user", foreground="#7C3AED", font=("Segoe UI",11,"bold"))
chat.tag_config("bot", foreground="#A855F7")
chat.config(state="disabled")

bottom = tk.Frame(right, bg="#FAF8FF")
bottom.pack(fill="x", padx=40, pady=20)

entry = tk.Entry(bottom, font=("Segoe UI", 13))
entry.pack(side="left", fill="x", expand=True, ipady=12)

tk.Button(
    bottom,
    text="🎵 Send",
    command=send_message,
    bg="#A855F7",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=25,
    pady=10
).pack(side="right", padx=10)

root.bind("<Return>", lambda e: send_message())
root.mainloop()