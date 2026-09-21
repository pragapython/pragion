Pragion.state = {
  presentation: new Map(),
  set(key, value) { this.presentation.set(key, value); },
  get(key) { return this.presentation.get(key); },
};
