// app.js

document.addEventListener("DOMContentLoaded", function () {
    const infoBox = document.getElementById("infoBox");

    // Bitki ya da hayvan hakkında bilgi gösterme
    async function fetchNatureInfo(species) {
        try {
            const response = await fetch(`https://api.example.com/nature/${species}`);
            const data = await response.json();
            infoBox.setAttribute("text", {
                value: `Tür: ${data.name}\nAçıklama: ${data.description}`,
                color: "green"
            });
        } catch (error) {
            console.error("Bilgi alınırken hata oluştu:", error);
            infoBox.setAttribute("text", {
                value: "Bilgi alınamadı.",
                color: "red"
            });
        }
    }

    // Görev önerisini bulanık mantık API'siyle alma
    async function fetchTaskSuggestion(interestLevel) {
        try {
            const response = await fetch("/suggest_task", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ interestLevel })
            });
            const data = await response.json();
            alert(`Önerilen Görev: ${data.suggestedTask}`);
        } catch (error) {
            console.error("Görev önerisi alınırken hata oluştu:", error);
        }
    }

    // Örnek tarama işlevi
    document.addEventListener("markerFound", () => {
        const species = "Çam Ağacı"; // Örnek
        fetchNatureInfo(species);
        fetchTaskSuggestion(0.8); // İlgi seviyesi örneği
    });
});
