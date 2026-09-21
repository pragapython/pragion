# Pragion UI Protocol

Frontend events use JSON-shaped messages:

```json
{
  "type": "event",
  "event": "button.click",
  "component_id": "login_button"
}
```

The browser runtime emits `CustomEvent` instances and future WebView adapters can serialize the detail object for the Python runtime. Messages must be validated by the receiving boundary. The protocol does not expose unrestricted native objects or arbitrary JavaScript execution.
