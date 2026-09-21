window.Pragion = window.Pragion || {};

Pragion.core = {
  init() {
    this.setTheme(localStorage.getItem("pragion-theme") || "system");
    document.querySelectorAll("[data-pragion-theme-choice]").forEach((control) => {
      control.addEventListener("click", () => this.setTheme(control.dataset.pragionThemeChoice));
    });
  },
  setTheme(theme) {
    document.documentElement.dataset.pragionTheme = theme;
    localStorage.setItem("pragion-theme", theme);
  },
};

document.addEventListener("DOMContentLoaded", () => Pragion.core.init());
