document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("conForm");

    form.addEventListener("submit", async(e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        try {
            const response = await fetch("https://hierarchy-attractive-foods-favor.trycloudflare.com/contact", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            })

            const result = await response.json();
            if (response.ok) {
                alert("Sent successful!");
                form.reset();
            } else {
                alert("Error: " + JSON.stringify(result));
            }
        } catch (err) {
            alert("t" + err);
        }
    });

    const btn = document.getElementById("menuBtn");
    const menu = document.getElementById("navMenu");

    btn.onclick = () => menu.classList.toggle("open");
    document.addEventListener("click", (e) => {
        if (!menu.contains(e.target) && !btn.contains(e.target)) {
            menu.classList.remove("open");
        }
    });
});