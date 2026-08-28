
//barebones stuff
document.querySelector("form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const response = await fetch("/generate", { method: "POST", body: new FormData(e.target) });
  const blob = await response.blob();
  // create a temporary link and click it to trigger the download
});