async function getQuote() {
  const quoteEl = document.getElementById("quote");
  const authorEl = document.getElementById("author");

  // Show loading state
  quoteEl.innerText = "Loading...";
  authorEl.innerText = "";

  try {
    const res = await fetch("/quote");
    const data = await res.json();

    // Update UI
    quoteEl.innerText = data.text;
    authorEl.innerText = "- " + data.author;

  } catch (err) {
    quoteEl.innerText = "Failed to load quote";
    authorEl.innerText = "";
  }
}

// Load quote when page opens
getQuote();