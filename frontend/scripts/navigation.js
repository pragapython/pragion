Pragion.navigation = {
  go(path) {
    window.history.pushState({}, "", path);
    Pragion.events.emit("navigation.change", { path });
  },
};
