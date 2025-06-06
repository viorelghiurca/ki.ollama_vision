# Ollama Vision Chat

Ein einfaches Python-Tool für die Interaktion mit Ollama Vision-Modellen. Verarbeite Bilder und erhalte strukturierte JSON-Antworten.

A simple Python wrapper for interacting with Ollama's vision models. Process images and get structured JSON responses.

## 📋 Voraussetzungen / Requirements

- Python 3.x
- Ollama mit Vision-Modellen lokal installiert
- `requests` Bibliothek

## 🚀 Installation

1. Abhängigkeiten installieren / Install dependencies:
```bash
pip install requests
```

2. Ollama mit Vision-Modellen starten (Standard-Port: 11434)

## 💻 Verwendung / Usage

### Kommandozeile / Command Line
```bash
python ollama_vision_chat.py
```

### Grafische Oberfläche / GUI
```bash
python gui.py
```

### Ordnerstruktur / Folder Structure
- `uploads/`: Hier Bilder ablegen / Place images here
- `processed/`: Verarbeitete Bilder / Processed images
- `results/`: JSON-Antworten / JSON responses

## ⚙️ Konfiguration / Configuration

- Standard-Modell / Default model: llama3.2-vision
- Temperatur / Temperature: 0.2
- Server-URL / Server URL: http://localhost:11434/api/generate (konfigurierbar / configurable)

## 🔒 Datenschutz & Sicherheit / Privacy & Security

Die Anwendung implementiert verschiedene Datenschutz- und Sicherheitsmaßnahmen:

The application implements several privacy and security measures:

- Alle Dateipfade werden bereinigt / All file paths are sanitized
- Sensible Daten in Antworten werden automatisch geschwärzt / Sensitive data in responses is automatically redacted
- API-Endpunkt ist konfigurierbar / API endpoint is configurable
- Bildnamen werden vor der Speicherung bereinigt / Image names are sanitized before storage
- Vollständige Dateipfade werden nie in der GUI angezeigt / Full file paths are never displayed in the GUI
- Zeitstempel werden in einem standardisierten Format gespeichert / Timestamps are stored in a standardized format

## 📊 Antwortformat / Response Format

Ergebnisse werden als JSON gespeichert mit / Results are saved as JSON with:
- Zeitstempel / Timestamp (YYYYMMDD_HHMMSS Format)
- Bereinigter Bildname / Sanitized image name
- Prompt
- Temperatur / Temperature
- Bereinigte Modellantwort / Sanitized model response

## 🛠️ Entwicklung / Development

### Code-Struktur / Code Structure
- `ollama_vision_chat.py`: Hauptlogik / Core logic
- `gui.py`: Grafische Benutzeroberfläche / Graphical user interface

### Erweiterungen / Extensions
Die Anwendung kann durch folgende Maßnahmen erweitert werden / The application can be extended by:
- Hinzufügen weiterer Modelle / Adding more models
- Anpassen der Datenschutzfilter / Customizing privacy filters
- Implementieren zusätzlicher Sicherheitsmaßnahmen / Implementing additional security measures

## 📝 Lizenz / License

MIT License 