Pragion.events = {
  emit(name, payload = {}) {
    const detail = { type: "event", event: name, ...payload };
    document.dispatchEvent(new CustomEvent("pragion:event", { detail }));
    return detail;
  },
};

document.addEventListener("click", (event) => {
  const action = event.target.closest("[data-pragion-action]");
  if (action) Pragion.events.emit(action.dataset.pragionAction, { component_id: action.id || null });
});
