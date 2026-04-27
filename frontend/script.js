document.getElementById("loanForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const btn = document.getElementById("submitBtn");
    const resultDiv = document.getElementById("result");

    // Show loading state
    btn.innerHTML = `<span>Processing...</span> <i class="fas fa-spinner fa-spin"></i>`;
    btn.style.opacity = "0.7";

    // Collect all data from form
    const data = {
        gender: parseInt(document.getElementById("gender").value),
        married: parseInt(document.getElementById("married").value),
        dependents: parseInt(document.getElementById("dependents").value),
        education: parseInt(document.getElementById("education").value),
        self_employed: 0, // Default rakha ha, aap field add kar saktay hain
        income: parseInt(document.getElementById("income").value),
        co_income: parseInt(document.getElementById("co_income").value),
        loan_amount: parseInt(document.getElementById("loan").value),
        loan_term: parseInt(document.getElementById("loan_term").value),
        credit: parseInt(document.getElementById("credit").value),
        area: 1 // Default: Semi-Urban
    };

    try {
        const res = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        const prob = (result.probability * 100).toFixed(2);

        resultDiv.style.display = "block";

        if (result.prediction === 1) {
            resultDiv.className = "result-card approved";
            resultDiv.innerHTML = `<i class="fas fa-check-circle"></i> Loan Approved! Confidence: ${prob}%`;
        } else {
            resultDiv.className = "result-card rejected";
            resultDiv.innerHTML = `<i class="fas fa-times-circle"></i> Application Rejected. Confidence: ${prob}%`;
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Flask Server se contact nahi ho pa raha!");
    } finally {
        btn.innerHTML = `<span>Verify Eligibility</span> <i class="fas fa-check"></i>`;
        btn.style.opacity = "1";
    }
});