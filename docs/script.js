document.getElementById('detectBtn').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value;
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = "Detecting...";

    try {
        const response = await fetch('https://homoglyph-detect.onrender.com/detect', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        if (!response.ok) {
            throw new Error('Server error');
        }

        const data = await response.json();

        if (data.is_suspicious) {
            let chars = data.suspicious_chars.map(
                c => `Character: "${c.original}" (Unicode: ${c.unicode}) looks like "${c.similar_to}"`
            ).join('<br>');
            resultDiv.innerHTML = `<b>Suspicious homoglyphs found:</b><br>${chars}`;
        } else {
            resultDiv.innerHTML = "✅ No suspicious homoglyphs detected!";
        }
    } catch (err) {
        resultDiv.textContent = "Error connecting to the server.";
    }
});
