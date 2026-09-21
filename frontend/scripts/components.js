Pragion.components = {
  dialog(id, open) {
    const element = document.getElementById(id);
    if (!element) return;
    element.dataset.open = String(open);
    element.setAttribute("aria-hidden", String(!open));
  },
  sheet(id, open) {
    const element = document.getElementById(id);
    if (!element) return;
    element.dataset.open = String(open);
    element.setAttribute("aria-hidden", String(!open));
  },
  tabs(root) {
    root.querySelectorAll("[role=tab]").forEach((tab) => {
      tab.addEventListener("click", () => {
        root.querySelectorAll("[role=tab]").forEach((item) => item.setAttribute("aria-selected", String(item === tab)));
        root.querySelectorAll("[role=tabpanel]").forEach((panel) => panel.hidden = panel.id !== tab.getAttribute("aria-controls"));
      });
    });
  },
};

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-pragion-tabs]").forEach((root) => Pragion.components.tabs(root));
});

document.addEventListener("pragion:event", (event) => {
  const { event: name } = event.detail;
  const actions = {
    "dialog.open": () => Pragion.components.dialog("demo-dialog", true),
    "dialog.close": () => Pragion.components.dialog("demo-dialog", false),
    "sheet.open": () => Pragion.components.sheet("demo-sheet", true),
    "sheet.close": () => Pragion.components.sheet("demo-sheet", false),
  };
  if (actions[name]) actions[name]();
});
