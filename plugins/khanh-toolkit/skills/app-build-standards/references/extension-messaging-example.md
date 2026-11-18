# Safe message handling in an MV3 extension

```js
// background.js (service worker) - validate who sent the message and what it contains
const ALLOWED_ACTIONS = new Set(["saveNote", "getNotes"]);

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  // 1. Only accept messages from this extension's own pages/content scripts
  if (sender.id !== chrome.runtime.id) return;

  // 2. Validate shape (use Zod/Valibot in real projects)
  if (typeof msg !== "object" || !ALLOWED_ACTIONS.has(msg.action)) return;

  if (msg.action === "saveNote") {
    if (typeof msg.text !== "string" || msg.text.length > 5000) {
      sendResponse({ ok: false, error: "invalid_input" });
      return;
    }
    // 3. Persist state - the service worker may be killed at any time, globals are lost
    chrome.storage.local.get({ notes: [] }).then(({ notes }) => {
      notes.push({ text: msg.text, url: sender.url, at: Date.now() });
      return chrome.storage.local.set({ notes });
    }).then(() => sendResponse({ ok: true }));
    return true; // keep the channel open for the async response
  }
});
```

```js
// content.js - the web page is hostile: never trust its DOM or postMessage blindly
window.addEventListener("message", (event) => {
  if (event.source !== window) return;                    // only same window
  if (event.origin !== "https://example.com") return;     // only expected origin
  const data = event.data;
  if (!data || data.type !== "MYEXT_SAVE" || typeof data.text !== "string") return;
  chrome.runtime.sendMessage({ action: "saveNote", text: data.text.slice(0, 5000) });
});

// Render UI safely inside a Shadow DOM (isolates styles from the page)
// and use textContent, never innerHTML with page-derived strings
const host = document.createElement("div");
const shadow = host.attachShadow({ mode: "closed" });
const badge = document.createElement("div");
badge.textContent = "Saved"; // safe: treated as text, not HTML
shadow.append(badge);
document.body.append(host);
```
