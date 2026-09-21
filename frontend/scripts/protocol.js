Pragion.protocol = {
  version: "0.0.5",
  event(name, componentId, payload = {}) {
    return { type: "event", event: name, component_id: componentId, payload };
  },
  isValid(message) {
    return Boolean(message && message.type === "event" && typeof message.event === "string" && typeof message.component_id !== "undefined");
  },
};
