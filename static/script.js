async function classifyWord() {
    const word = document.getElementById('word').value;
    if (!word) {
        document.getElementById('result').innerText = 'يرجى إدخال كلمة.';
        return;
    }

    try {
        const response = await fetch('/classify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ word: word }),
        });

        const data = await response.json();
        document.getElementById('result').innerText = data.result;
    } catch (error) {
        document.getElementById('result').innerText = 'حدث خطأ أثناء تحليل الكلمة.';
        console.error('Error:', error);
    }
}
