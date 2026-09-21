Pragion.api = {
  async getCustomer(id) {
    const response = await fetch(`/api/customers/${encodeURIComponent(id)}`, { headers: { Accept: "application/json" } });
    if (!response.ok) throw new Error("Unable to load customer");
    return response.json();
  },
};
