# 🚀 Parakram GATE 2026 Dashboard

A high-performance, custom-built Learning Management System (LMS) dashboard designed specifically for **GATE 2026 (CS & IT)** aspirants. This project features a sophisticated "Direct Stream" injection system to bypass standard cloud storage processing delays and "virus scan" interstitials.

![Tech](https://img.shields.io/badge/Tech-Vanilla%20JS%20%7C%20CSS3%20%7C%20HTML5-blueviolet)
![Focus](https://img.shields.io/badge/Focus-GATE%202026-red)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🎯 The Core Problem & Solution

**The Problem:** Standard Google Drive video links often show a "Still Processing" error for high-bitrate lectures, and the default UI lacks a professional educational interface (simultaneous access to DPPs, notes, and playlists).

**The Solution:** This dashboard uses a **Triple-Failover Streaming Logic**. It intercepts the Google Drive file ID and attempts to stream the raw data directly into a custom HTML5 player. This provides:
1. **Instant Playback:** No waiting for Drive to "process" the video.
2. **Buffer Optimization:** Manual handling of buffer states and loading timeouts.
3. **Failover Security:** Automatically switches to Iframe embed if the direct stream is blocked.

---

## ✨ Key Features

### 📺 Advanced Video Player
* **Direct Stream Injection:** Uses `confirm=t` parameters to bypass security prompts for large video files.
* **Smart UI Overlay:** Custom controls, mode badges (DIRECT vs IFRAME), and "Open in Drive" shortcuts.
* **Auto-Navigation:** Seamless "Next" and "Previous" lecture controls that sync across the batch hierarchy.

### 🔍 Search & Organization
* **Global Search (ESC):** A lightning-fast search overlay to find any topic across all 19 subjects instantly.
* **Breadcrumb System:** Intuitive navigation from `Batch` ➔ `Subjects` ➔ `Chapters` ➔ `Player`.
* **Integrated Attachments:** Quick-access modals for Class Notes, DPP PDFs, and DPP Video Solutions.

### 🎨 Premium UI/UX
* **Typography:** Optimized with *Plus Jakarta Sans* for long study sessions.
* **Dark-Mode Native:** Deep-space palette (`#0b0d14`) to reduce eye strain during late-night study grinds.
* **Responsive:** Fully functional on mobile for quick revisions between college classes or during gym breaks.

---

## 🛠️ Technical Implementation

### Streaming Engine (`script.js`)
The engine prioritizes raw file access to ensure the highest possible quality without Drive's compression:
```javascript
const STREAM_URLS = id => [
  `https://drive.google.com/uc?export=download&id=${id}&confirm=t`,
  `https://drive.usercontent.google.com/download?id=${id}&export=download&authuser=0&confirm=t`
];


