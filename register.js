document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("regForm");

    form.addEventListener("submit", async(e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch("https://patient-soundtrack-romantic-leonard.trycloudflare.com/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                alert("Registration successful!");
                form.reset();
            } else {
                alert("Error: " + JSON.stringify(result));
            }
        } catch (err) {
            alert("" + err);
        }
    });

    // Drawer toggle
    const btn = document.getElementById("menuBtn");
    const menu = document.getElementById("navMenu");

    btn.addEventListener("click", () => menu.classList.toggle("open"));
    document.addEventListener("click", (e) => {
        if (!menu.contains(e.target) && !btn.contains(e.target)) {
            menu.classList.remove("open");
        }
    });
});